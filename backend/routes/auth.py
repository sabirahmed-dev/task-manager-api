from fastapi import Depends ,HTTPException
from fastapi.security import HTTPBearer ,HTTPAuthorizationCredentials
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from jose import jwt
import logging
import os


from backend.schemas.user_schema import userCreate
from backend.models.user_model import User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

security = HTTPBearer()


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
    )


def register_user(user_data :userCreate,db :Session):

    user = db.query(User).filter(User.email == user_data.email).first()

    if user:
        logger.warning("User alredy exists")
        raise HTTPException(
            status_code=409,
            detail ="Email already exist"
            )


    hashed_password = pwd_context.hash(user_data.password)

    user = User(
        email = user_data.email,
        password = hashed_password
        )

    db.add(user)
    db.commit()

    logger.info("User has been regiested")
    return {"messege":"user has been added"},200

def login_user(user_data :userCreate,db :Session):

    user = db.query(User).filter(User.email == user_data.email).first()

    if not user:
        logger.warning("Invalid email")
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
            )

    if not pwd_context.verify(user_data.password,user.password):
        logger.warning("invaild password")
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
            )

    payload ={
        "sub":str(user.id)
        }

    secret_key = os.getenv("SECRET_KEY")

    token = jwt.encode(
        payload,
        secret_key,
        algorithm="HS256"
        )
    logger.info(token)
    return token


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
    ):

    token = credentials.credentials

    try:
        secret_key = os.getenv("SECRET_KEY")
        payload = jwt.decode(token,secret_key,algorithms=["HS256"])
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=401,
            detail="invaild token or secret_key"
            )
    logger.info("payload has been created")
    return payload







