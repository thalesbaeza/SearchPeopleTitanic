from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import database_models, schemas
from app.config.database import get_db
from app.models.schemas import PersonCreate, PersonResponse
from app.models.database_models import TitanicPassenger

router = APIRouter(tags=["Passengers"])

@router.post("/create", response_model=PersonResponse)
def create_person(person: PersonCreate, db: Session = Depends(get_db)):
    db_person = TitanicPassenger(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

@router.get("/search/{person_id}", response_model=schemas.PersonResponse)
def read_person(person_id: int, db: Session = Depends(get_db)):
    db_person = db.query(database_models.TitanicPassenger).filter(database_models.TitanicPassenger.id == person_id).first()
    if not db_person:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

@router.put("/update/{person_id}", response_model=schemas.PersonResponse)
def update_person(person_id: int, updated_person: schemas.PersonCreate, db: Session = Depends(get_db)):
    db_person = db.query(database_models.TitanicPassenger).filter(database_models.TitanicPassenger.id == person_id).first()
    if not db_person:
        raise HTTPException(status_code=404, detail="Person not found")
    for key, value in updated_person.dict().items():
        setattr(db_person, key, value)
    db.commit()
    db.refresh(db_person)
    return db_person

@router.delete("/delete/{person_id}")
def delete_person(person_id: int, db: Session = Depends(get_db)):
    db_person = db.query(database_models.TitanicPassenger).filter(database_models.TitanicPassenger.id == person_id).first()
    if not db_person:
        raise HTTPException(status_code=404, detail="Person not found")
    db.delete(db_person)
    db.commit()
    return {"detail": "Person deleted"}