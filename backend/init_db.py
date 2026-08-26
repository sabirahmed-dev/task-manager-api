from backend.database import engine
from backend.models import Base

def init_db():
    Base.metadata.create_all(bind=engine) 
