# SearchPeopleTitanic

**Descrição**

A SearchPeopleTitanic API é uma aplicação construída em FastAPI que permite minerar dados do Titanic a partir de páginas HTML, armazená-los em um banco de dados PostgreSQL e gerenciar essas informações (criar, buscar, atualizar e deletar passageiros).

**Recursos**

HTML Scraping: Mineração de dados sobre passageiros e tripulação do Titanic a partir de páginas externas usando BeautifulSoup.

Persistência em Banco de Dados: Armazenamento dos dados minerados em um banco PostgreSQL.

CRUD Completo: Endpoints para criar, buscar, atualizar e deletar registros de passageiros.
    Estruturado em Módulos:

        Configuração do banco de dados e ambiente.

        Rotas dedicadas para CRUD e mineração de HTML.
        
        Modelos SQLAlchemy para persistência e Schemas Pydantic para validação.

**Tecnologias**

    Python (3.12)
    FastAPI
    SQLAlchemy
    Pydantic
    BeautifulSoup (para scraping de HTML)
    PostgreSQL (banco de dados)
    Docker e Docker Compose


## **Endpoints**

| **Método** | **Endpoint**              | **Descrição**                                         |
|------------|---------------------------|------------------------------------------------------|
| `POST`     | `/html/mine_list`         | Minera dados de passageiros a partir de um URL.      |
| `POST`     | `/html/mine_passenger`    | Minera dados de um passageiro específico.            |
| `POST`     | `/Passenger/create`       | Cria um novo passageiro.                             |
| `GET`      | `/Passenger/search/{id}`  | Busca um passageiro pelo ID.                         |
| `PUT`      | `/Passenger/update/{id}`  | Atualiza os dados de um passageiro.                  |
| `DELETE`   | `/Passenger/delete/{id}`  | Deleta um passageiro pelo ID.                        |
| `GET`      | `/`                       | Verifica se a API está rodando.                      |


**Estrutura do Projeto**

```bash
SearchPeopleTitanic/
├── app/
│   ├── config/          # Configurações do banco e aplicação
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── settings.py
│   ├── models/          # Modelos SQLAlchemy e Schemas Pydantic
│   │   ├── __init__.py
│   │   ├── database_models.py
│   │   └── schemas.py
│   ├── routes/          # Rotas da API
│   │   ├── __init__.py
│   │   ├── crud_routes.py
│   │   └── html_routes.py
│   └── main.py          # Ponto de entrada principal da aplicação
├── .env                 # Variáveis de ambiente
├── docker-compose.yml   # Configuração do Docker Compose
├── Dockerfile           # Configuração do contêiner Docker
├── requirements.txt     # Dependências da aplicação
└── README.md            # Documentação do projeto
```