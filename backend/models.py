from sqlalchemy import Integer,Column,String
from backend.database import Base

class Task(Base):
    __tablename__="tasks"

    id = Column(Integer,primary_key=True)
    task = Column(String)
    status = Column(String)
