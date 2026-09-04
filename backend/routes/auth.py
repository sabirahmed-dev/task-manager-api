from fastapi import Depends ,HTTPException
from fastapi.security import HTTPBearer ,HTTPAuthorizationCredentials
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from jose import jwt
import os


from backend.schemas.user_schema import userCreate
from backend.models.user_model import User

security = HTTPBearer()


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
    )


def register_user(user_data :userCreate,db :Session):

    hashed_password = pwd_context.hash(user_data.password)

    user = User(
        email = user_data.email,
        password = hashed_password
        )

    db.add(user)
    db.commit()

    return {"messege":"user has been added"},200

def login_user(user_data :userCreate,db :Session):

    user = db.query(User).filter(User.email == user_data.email).first()

    if not user:
        return {"messege":"incorrect credentials"}

    if not pwd_context.verify(user_data.password,user.password):
        return {"messege":"icorrect password"}

    payload ={
        "sub":str(user.id)
        }

    secret_key = os.getenv("SECRET_KEY")

    token = jwt.encode(
        payload,
        secret_key,
        algorithm="HS256"
        )

    return token


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
    ):
    
    token = credentials.credentials

    try:
        secret_key = os.getenv("SECRET_KEY")
        payload = jwt.decode(token,secret_key,algorithms=["HS256"])
    except:
        raise HTTPException(
            status_code=401,
            detail="invaild token"
            )

    return payload
        
        
    

    
                
    
