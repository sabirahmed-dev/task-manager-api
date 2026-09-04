from sqlalchemy import Column,Integer,String
from backend.database import Base

class User(Base):
    __tablename__ ="Users"

    id = Column(Integer,primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String(266) ,nullable=False)
