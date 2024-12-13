from fastapi import FastAPI
from app.config.database import engine
from app.models.database_models import Base
from app.routes.crud_routes import router as people_router
from app.routes.html_routes import router as html_router

app = FastAPI(
    title="SearchPeopleTitanic API",
    description="API to find people from Titanic through data mined from HTML. Persist data in postgresql database",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(people_router, prefix="/passenger")
app.include_router(html_router, prefix="/html")

@app.get("/")
def root():
    return {"message": "SearchPeopleTitanic API is running!!"}