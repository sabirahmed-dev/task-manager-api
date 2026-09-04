import backend.models.user_model
import backend.models
from backend.database import engine ,Base

def init_db():
    Base.metadata.create_all(bind=engine) 
