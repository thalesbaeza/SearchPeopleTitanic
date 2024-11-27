from urllib.request import Request, urlopen
from urllib.request import URLError, HTTPError
from bs4 import BeautifulSoup
from config import conexao

conectar = conexao.Conexao()



link = 'https://www.encyclopedia-titanica.org/titanic-victim/jego-grga-cacic.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

#listaocupacao = ['Senior 6th. Engineer','2nd. Class Cook','2nd Baker','Junior Assistant 2nd. Engineer','Bed Room Steward (1st class)','Deck Engineer','Assistant baker','Assistant Vegetable Cook','Assistant Waiter','Smoke Room Steward (1st class)','Assistant Second Steward','Assistant Barber','Glory hole steward','Bath Steward','3rd Class Packer Steward','Third Class Steward','Smoke Room Steward (2nd Class)','Bathroom Steward (1st Class)','Assistant Saloon Steward, 2nd Class','Saloon Steward','Assistant Pantryman Steward','Squash racquet court attendant','First class saloon steward','Lounge Pantry Steward','Master-at-arms','Boatswain','Surgeon','Deck storekeeper','Able-bodied Seaman','Seaman','Assistant Surgeon','Mess Steward','Boatswain Mate','Lamp Trimmer','Lookout','Window Cleaner','Chief Officer','3rd. Officer','1st. Officer','6th. Officer','5th. Officer','2nd. Officer','4th. Officer','Master','Able Seaman','Saloon Steward','Realtor','Academic','Advertising Consultant','Architect','Artist','Aviator','Baggage Steward','Baker','Banker','Barber','Barman','Bath Attendant','Bell Boy','Bibliophile','Blacksmith','Boilermaker','Boots','Box Maker','Bricklayer','Builder','Bus Driver','Businessman','Butcher',"Butcher's Assistant",'Butler','Buyer','Cab Driver','Cabinet Maker','Carman','Carpenter / Joiner','Carver','Cashier','Caster','Chauffeur','Chef','Chemist','China Clay Worker','Cinematographer','Civil Servant','Clerk','Coach Trimmer','Confectioner','Cook','Cook (Personal)','Cooper','Crane Operator','Dairy Worker','Dealer','Decorator','Dipper','Doctor','Draughtsman','Dressmaker / Couturiere','Electrical Engineer','Electrician','Engineer','Estate Manager','Factory Foreman','Farm Labourer','Farmer','Farrier','Financier','Fireman','Fisherman','Fitter','Florist','Framer','Fur Cutter','Gambler','Gardener','General Labourer','Gentleman','Glass Man','Glove Cutter','Governess','Greaser','Grocer','Grocers Assistant','Groom','Horse Trainer','Hospital Attendant','Hospital Matron','Hotelier','Housekeeper','Housewife','Ice Man','Inspector','Interpreter','Ironmonger','Ironworker','Jeweller','Journalist','Judge','Justice of the Peace','Lamp Trimmer','Landowner','Laundry Worker','Lawyer','Leather Worker','Librarian','Lift Attendant','Linenkeeper','Locksmith','Machine Inspector','Magazineer','Manufacturer','Mason','Mechanical Engineer','Merchant','Messenger','Metallurgist','Military','Milliner','Miner','Missionary','Motor Fitter','Musical Instrument Vendor','Musician','Naval Architect','Nurse','Nursemaid','Of Independent Means','Oil Worker','Page Boy','Painter & Decorator','Pantryman','Personal Maid','Plateman','Plumber','Police Officer','Politician','Porter','Postal Clerk / Postman','Potter','Priest / Minister','Printer / Compositor','Property Developer / Real Estate','Provision Manager','Pugilist','Purser','Quarryman','Receptionist','Restaurant Manager','Retired','Saddler','Sales Manager','Salesman','Scholar','Scullion / Scullery Maid','Sculptor','Seaman','Seamstress','Secretary','Servant','Settler Recruiter',"Ship's Offier",'Shipbuilder','Shipowner','Shoemaker','Shop Assistant','Singer','Socialite','Sports Instructor','Sportsman','Stenographer','Steward','Stockbroker','Stockman','Stoker','Stone Cutter','Storekeeper','Tailor','Teacher','Telegraphist','Telephonist','Theatre Manager','Tile Maker','Tinsmith','Tool Maker','Tradesman','Traveller','Trimmer','Turner','Upholsterer','Valet','Waiter','Window Cleaner','Wood Carver','Writer']

try:
        req = Request(link, headers = headers)
        response = urlopen(req)
        html = response.read()
    
        html = html.decode('UTF-8')
    
        html = " ".join(html.split()).replace('> <', '><')

        soup = BeautifulSoup(html, 'html.parser')

        #NOME COMPLETO
        if str(soup.findAll('strong')).find('<strong>Name</strong>') > 0:
            prefix = str(soup.findAll('span', {"itemprop":"honorificPrefix"}))
            prefix = prefix.replace('[<span itemprop="honorificPrefix">',"").replace("</span>]","").replace('<span itemprop="honorificPrefix">',"").replace("</span>","")
    
            nome = str(soup.findAll('span', {"itemprop":"givenName"}))
            nome = nome.replace('[<span itemprop="givenName">',"").replace("</span>]","").replace('<span itemprop="givenName">',"").replace("</span>","")

            nomefamilia = str(soup.findAll('span', {"itemprop":"familyName"}))
            nomefamilia = nomefamilia.replace('[<span itemprop="familyName">',"").replace("</span>]","").replace('<span itemprop="familyName">',"").replace("</span>","").replace(", Mr","").replace(", Theodor","").replace("a labourer from, Kraeff","").replace(' a labourer from</span>, <span itemprop="familyName">Kraeff',"")

            nomecompleto = prefix.replace(", Mr","").replace(", Theodor","").replace(" a labourer from, Kraeff","") +' '+ nome.replace(", Mr","").replace(", Theodor","").replace(" a labourer from, Kraeff","") +' '+ nomefamilia.replace(", Mr","").replace(", Theodor","").replace(" a labourer from, Kraeff","").replace(' a labourer from</span>, <span itemprop="familyName">Kraeff',"")

        else:
            nomefamilia = 'None'
            nomecompleto= 'None'

        #IDADE
              
        
        if str(soup.findAll('strong')).find('Age') > 0:
            idade = str(soup.findAll('a'))
            if idade[idade.find('/titanic-ages/'):idade.find('/titanic-ages/')+21].replace("/titanic-ages/","").replace(".html","").strip() == '':
                idade = '-1'
            else:
                idade = idade[idade.find('/titanic-ages/'):idade.find('/titanic-ages/')+21].replace("/titanic-ages/","").replace(".html","").replace('"',"").strip()
        else:
            idade = ''

        #NOME DA FAMILIA
        nomefamilia = str(soup.findAll('span', {"itemprop":"familyName"}))
        nomefamilia = nomefamilia.replace('[<span itemprop="familyName">',"").replace("</span>]","").replace('<span itemprop="familyName">',"").replace("</span>","").replace(", Mr","").replace(", Theodor","").replace("a labourer from, Kraeff","").replace(' a labourer from</span>, <span itemprop="familyName">Kraeff',"")

        #GENERO
        if str(soup.findAll('span', {"itemprop":"gender"})).find('gender') > 0:
            genero = str(soup.findAll('span', {"itemprop":"gender"}))
            genero = genero.replace('[<span itemprop="gender">',"").replace("</span>]","")
        else:
            genero = 'None'

        #NACIONALIDADE
        
        if str(soup.find('span', {"itemprop":"nationality"})).find('nationality') > 0:
            nacionalidade = str(soup.find('span', {"itemprop":"nationality"}))
            nacionalidade = nacionalidade.replace('<span itemprop="nationality">',"").replace("</span>","").replace('[',"").replace(']',"")
        else:
            nacionalidade = 'None'

        #CLASS
        if str(soup.findAll('a')).find('1st Class Passengers') > 0:
            classocial = '1st Class Passengers'
        elif str(soup.findAll('a')).find('Titanic Engineering Crew') > 0:
            classocial = 'Engineering Crew'
        elif str(soup.findAll('a')).find('2nd Class Passengers') > 0:
            classocial='2nd Class Passengers'
        elif str(soup.findAll('a')).find('3rd Class Passengers') > 0:
            classocial = '3rd Class Passengers'
        elif str(soup.findAll('a')).find('Victualling Crew') > 0:
            classocial = 'Victualling Crew'
        elif str(soup.findAll('a')).find('Deck Crew') > 0:
            classocial = 'Deck Crew'
        elif str(soup.findAll('a')).find('Restaurant Crew') > 0:
            classocial = 'Restaurant Crew'
        else:
            classocial = 'None'  

        #EMBARKED
        if str(soup.findAll('a')).find('Titanic passengers and crew that embarked at Cherbourg') > 0:
            embarque = 'Cherbourg'
        elif str(soup.findAll('a')).find('Titanic passengers and crew that embarked at Southampton') > 0:
            embarque = 'Southampton'
        elif str(soup.findAll('a')).find('Titanic passengers and crew that embarked at Queenstown') > 0:
            embarque = 'Queenstown'
        elif str(soup.findAll('a')).find('Titanic passengers and crew that embarked at Belfast') > 0:
            embarque = 'Belfast'
        else:
            embarque = 'None'
        
        #DISEMBARKED
        if str(soup.findAll('strong')).find('Disembarked Carpathia') > 0:
            desembarque = 'New York City'
        elif str(soup.findAll('a')).find('href="/titanic-passengers-crew-disembarked/2/cherbourg.html"') > 0:
            desembarque = 'Cherbourg'
        elif str(soup.findAll('a')).find('href="/titanic-passengers-crew-disembarked/3/queenstown.html"') > 0:
            desembarque = 'Queenstown'
        elif str(soup.findAll('a')).find('href="/titanic-passengers-crew-disembarked/1/southampton.html"') > 0:
            desembarque = 'Southampton'
        elif str(soup.findAll('a')).find('href="/titanic-passengers-crew-disembarked/60/belfast.html"') > 0: 
            desembarque = 'Belfast'
        else:
            desembarque= 'None'

        #CASAMENTO
        if str(soup.findAll('a')).find('List of unmarried Titanic passengers and crew') > 0:
            parceiro= 'Single'
        elif str(soup.findAll('a')).find('List of engaged Titanic passengers and crew') > 0:
            parceiro = 'Engaged' 
        elif str(soup.findAll('a')).find('List of married Titanic passengers and crew') > 0:
            parceiro = 'Married'
        elif str(soup.findAll('a')).find('List of divorced Titanic passengers and crew') > 0:
            parceiro = 'Divorced' 
        else:
            parceiro = 'None'
        
        #RESGATADA
        if str(soup.findAll('strong')).find('Died in the Titanic disaster') > 0:
            resgate = 'Die'
        elif str(soup.findAll('strong')).find('Rescued') > 0:
            resgate = 'Rescued'
        else:
            resgate = 'None'

        #BOAT

        if str(soup.findAll('a')).find('Titanic survivors in lifeboat A') > 0:
            bot = 'lifeboat A'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat B') > 0:
            bot = 'lifeboat B'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat C') > 0:
            bot = 'lifeboat C'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat D') > 0:
            bot = 'lifeboat D'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat 1 ') > 0:
            bot = 'lifeboat 1'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat 2') > 0:
            bot = 'lifeboat 2'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat 3') > 0:
            bot = 'lifeboat 3'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat 4') > 0:
            bot = 'lifeboat 4'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat 5') > 0:
            bot = 'lifeboat 5'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat 6') > 0:
            bot = 'lifeboat 6'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat 7') > 0:
            bot = 'lifeboat 7'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat 8') > 0:
            bot = 'lifeboat 8'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat 9') > 0:
            bot = 'lifeboat 9'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat 10') > 0:
            bot = 'lifeboat 10'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat 11') > 0:
            bot = 'lifeboat 11'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat 12') > 0:
            bot = 'lifeboat 12'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat 13') > 0:
            bot = 'lifeboat 13'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat 14') > 0:
            bot = 'lifeboat 14'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat 15') > 0:
            bot = 'lifeboat 15'
        elif str(soup.findAll('a')).find('Titanic survivors in lifeboat 16') > 0:
            bot = 'lifeboat 16'
        else:
            bot = 'None'

        if str(soup.findAll('a')).find('Titanic passengers and crew that worked as') > 0:
            ocupacao = str(soup.find('span', {"itemprop":"jobTitle"}))
            ocupacao = ocupacao.replace('<span itemprop="jobTitle">',"").replace("</span>","").replace('[',"").replace(']',"")
        else:
            ocupacao = 'None'

        #OCUPACAO
        if str(soup.findAll('a')).find('Titanic passengers and crew that worked as') > 0:
            ocupacao = str(soup.find('span', {"itemprop":"jobTitle"}))
            ocupacao = ocupacao.replace('<span itemprop="jobTitle">',"").replace("</span>","").replace('[',"").replace(']',"")
        else:
            ocupacao = 'None'
                
        #CORPOS NÃO ENCONTRADOS
        if str(soup.findAll('strong')).find('Body Not Recovered') > 0:
            corposnaoencontrando = 'Body Not Recovered'
        else:
            corposnaoencontrando= 'Body Recovered'


        #conectar.criar('''CREATE TABLE IF NOT EXISTS titanic_people (NomeCompleto  TEXT, NomeFamilia TEXT, Idade TEXT, Genero TEXT, Nacionalidade TEXT, Embarque TEXT, Desembarque TEXT, Classocial TEXT, Parceiro TEXT, Resgate TEXT, Boat TEXT, Ocupacao TEXT, Corpos TEXT) ''')

        dataset = [nomecompleto, nomefamilia, idade, genero, nacionalidade, embarque, desembarque, classocial, parceiro, resgate, bot, ocupacao, corposnaoencontrando]

        print(dataset)

        #conectar.inserir('''INSERT INTO titanic_people (NomeCompleto, NomeFamilia, Idade, Genero, Nacionalidade, Embarque, Desembarque, Classocial, Parceiro, Resgate, Boat, Ocupacao, Corpos) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ''', dataset)


        
except:
        print('fodeu')