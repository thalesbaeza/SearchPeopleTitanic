from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PersonCreate(BaseModel):
    name: str
    family: str
    age: int
    gender: str
    nationality: str
    embarked: str
    disembarked: Optional[str]
    class_type: str
    marital_status: str
    rescued: str
    boat: Optional[str]
    occupation: str
    body: str
    link: Optional[str]

class PersonResponse(PersonCreate):
    id: int

    class Config:
        orm_mode = True
