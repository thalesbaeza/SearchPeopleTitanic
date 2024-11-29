from fastapi import APIRouter, Depends
from bs4 import BeautifulSoup
import json
from sqlalchemy.orm import Session
from app.models import database_models, schemas
from app.config.database import get_db
from urllib.request import Request, urlopen
from urllib.request import URLError, HTTPError
from app.models.schemas import PersonCreate
from app.routes.crud_routes import create_person, read_person, update_person, delete_person

router = APIRouter(tags=["HTML Scraper"])


@router.post('/mine_list')
def generate_list(url: str):
    passenger_list = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
    
    try:
        request = Request(url, headers=headers)
        response = urlopen(request)
        html = response.read()
        html = html.decode('UTF-8')
        html = " ".join(html.split()).replace('> <', '><')
        
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.findAll('a', {"itemprop": "url"}):
            href = item.get('href')
            if href:
                mine_html_page(href)
                print(href)
                passenger_list.append({"url": href})

        return {"passengers": passenger_list}

    except HTTPError as e:
        raise HTTPException(status_code=e.code, detail=f"HTTP Error: {e.reason}")
    except URLError as e:
        raise HTTPException(status_code=500, detail=f"URL Error: {e.reason}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


def extract_passenger_data(soup, link):
    def extract_text(selector, attribute=None, default="None"):
        element = soup.find(selector, attribute) if attribute else soup.find(selector)
        return element.text.strip() if element else default

    def classify_by_keywords(tag, keywords, default="None"):
        content = str(soup.find_all(tag))
        for keyword, classification in keywords.items():
            if keyword in content:
                return classification
        return default

    # Name
    prefix = extract_text("span", {"itemprop": "honorificPrefix"})
    first_name = extract_text("span", {"itemprop": "givenName"})
    family_name = extract_text("span", {"itemprop": "familyName"})
    full_name = f"{prefix} {first_name} {family_name}".strip() or "None"

    # Age
    age_tag = soup.find_all("a")
    age = next(
        (
            age.get("href").replace("/titanic-ages/", "").replace(".html", "").strip()
            for age in age_tag
            if "/titanic-ages/" in str(age)
        ),
        "-1",
    )

    # Gender
    gender = extract_text("span", {"itemprop": "gender"})

    # Nationality
    nationality = extract_text("span", {"itemprop": "nationality"})

    # social_class
    class_mapping = {
        "1st Class Passengers": "1st Class",
        "2nd Class Passengers": "2nd Class",
        "3rd Class Passengers": "3rd Class",
        "Titanic Engineering Crew": "Engineering Crew",
        "Victualling Crew": "Victualling Crew",
        "Deck Crew": "Deck Crew",
        "Restaurant Crew": "Restaurant Crew",
    }
    social_class = classify_by_keywords("a", class_mapping)

    # embark
    embark_mapping = {
        "embarked at Cherbourg": "Cherbourg",
        "embarked at Southampton": "Southampton",
        "embarked at Queenstown": "Queenstown",
        "embarked at Belfast": "Belfast",
    }
    embark = classify_by_keywords("a", embark_mapping)

    # disembark
    disembark_mapping = {
        "Disembarked Carpathia": "New York City",
        'href="/titanic-passengers-crew-disembarked/2/cherbourg.html"': "Cherbourg",
        'href="/titanic-passengers-crew-disembarked/3/queenstown.html"': "Queenstown",
        'href="/titanic-passengers-crew-disembarked/1/southampton.html"': "Southampton",
        'href="/titanic-passengers-crew-disembarked/60/belfast.html"': "Belfast",
    }
    disembark = classify_by_keywords("a", disembark_mapping)
    
    if disembark == "None":
        disembark = classify_by_keywords("strong", disembark_mapping)
    else:
        disembark== "None"
    
    # marital_status
    marital_mapping = {
        "unmarried Titanic passengers": "Single",
        "engaged Titanic passengers": "Engaged",
        "married Titanic passengers": "Married",
        "divorced Titanic passengers": "Divorced",
        "widowed Titanic passengers": "Widowed",
    }
    marital_status = classify_by_keywords("a", marital_mapping)

    # rescue_status
    rescue_mapping = {
        "Died in the Titanic disaster": "Lost",
        "Rescued": "Saved",
    }
    rescue_status = classify_by_keywords("strong", rescue_mapping)

    # boat
    boat_mapping = {f"lifeboat {chr(i)}": f"lifeboat {chr(i)}" for i in range(65, 91)}
    boat_mapping.update({f"lifeboat {i}": f"lifeboat {i}" for i in range(1, 17)})
    boat = classify_by_keywords("a", boat_mapping)

    # occupation
    if str(soup.findAll('a')).find('Titanic passengers and crew that worked as') > 0:
        occupation = str(soup.find('span', {"itemprop":"jobTitle"}))
        occupation = occupation.replace('<span itemprop="jobTitle">',"").replace("</span>","").replace('[',"").replace(']',"")
    else:
        occupation = 'None'

    # body_status
    body_status = (
        "Body Not Identified"
        if "Body Not Identified" in str(soup.find_all("strong"))
        else "Body Recovered"
    )

    # create
    Json = {
        "name": full_name,
        "family": family_name,
        "age": age,
        "gender": gender,
        "nationality": nationality,
        "embarked": embark,
        "disembarked": disembark,
        "class_type": social_class,
        "marital_status": marital_status,
        "rescued": rescue_status,
        "boat": boat,
        "occupation": occupation,
        "body": body_status,
        "link": link
        }
    
    db: Session = next(get_db())

    person = PersonCreate(**Json)

    result = create_person(person=person, db=db)
    print(result)
@router.post("/mine_passenger")
def mine_html_page(name: str):
    link = 'https://www.encyclopedia-titanica.org' + name
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
    
    try:
        request = Request(link, headers=headers)
        response = urlopen(request)
        html =response.read()
        html = html.decode('UTF-8')
        html = " ".join(html.split()).replace('> <', '><')
        soup = BeautifulSoup(html, 'html.parser')
        extract_passenger_data(soup, link)
    except:
        print("Error when entering passenger data into the database!")
