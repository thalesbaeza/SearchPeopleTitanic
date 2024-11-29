from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TitanicPassenger(Base):
    __tablename__ = "titanic_passengers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    family = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)
    nationality = Column(String, nullable=False)
    embarked = Column(String, nullable=False)
    disembarked = Column(String, nullable=True)
    class_type = Column(String, nullable=False)
    marital_status = Column(String, nullable=False)
    rescued = Column(String, nullable=False)
    boat = Column(String, nullable=True)
    occupation = Column(String, nullable=False)
    body = Column(String, nullable=False)
    link = Column(Text, nullable=True)