from urllib.request import Request, urlopen
from urllib.request import URLError, HTTPError
from bs4 import BeautifulSoup
from models import bs4_encontrar_pessoas
from dotenv import load_dotenv


load_dotenv()

url = 'https://www.encyclopedia-titanica.org/titanic-maiden-voyage-passengers-and-crew/'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

lista = []

try:
  req = Request(url, headers = headers)
  response = urlopen(req)
  html = response.read()
  
  html = html.decode('UTF-8')
  
  html = " ".join(html.split()).replace('> <', '><')

  soup = BeautifulSoup(html, 'html.parser')

  for item in soup.findAll('a', {"itemprop":"url"}):
      lista.append(item.get('href'))

  for nome_pessoa in lista:
    print(nome_pessoa)
    bs4_encontrar_pessoas.search_peaple(nome_pessoa)


except HTTPError as e:
  print(e.status, e.reason)

except URLError as e:
  print(e.status, e.reason)


