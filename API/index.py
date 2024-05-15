import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta, timezone
from typing import Annotated, Union
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
import random as r

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)


class DierBase(BaseModel):
    naam: str
    soort: int
    foto: str
    geslacht: str
    ras: str
    commentaar: str
    geboorte_datum: str


class SoortBase(BaseModel):
    naam: str


class ReserveringBase(BaseModel):
    dier_id: int
    gebruiker_id: int


class UserBase(BaseModel):
    username: str
    password: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 0.5

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

db_dependency = Annotated[Session, Depends(get_db)]


class UserInDB(UserBase):
    user_id: int


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_user_by_username(db: Session, username: str):
    return db.query(models.users).filter(models.users.username == username).first()


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False

    return user


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    db = SessionLocal()
    user = get_user_by_username(db, username)
    db.close()
    if user is None:
        raise credentials_exception
    return user


@app.post('/users/', status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.users(**user.dict())
    db_user.password = pwd_context.hash(db_user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/users/login")
async def login(user: UserBase):
    db = SessionLocal()
    user = authenticate_user(db, user.username, user.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "gebruiker_id": user.gebruiker_id,
        "username": user.username,
        "password": user.password,
    }


@app.get("/users/me")
async def read_users_me(current_user: UserInDB = Depends(get_current_user)):
    return current_user


@app.get('/refresh')
async def get_new_acces_token(username: str):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": username}, expires_delta=access_token_expires)
    return {"access_token": access_token}


@app.get('/dieren', status_code=status.HTTP_200_OK)
async def get_alle_dieren(db: db_dependency, soort: int, ):
    return db.query(models.Dier).where(models.Dier.soort == soort).all()


@app.get("/dier", status_code=status.HTTP_200_OK)
async def get_dier(db: db_dependency, limit: int, offset: int, soort: int,
                   current_user: UserInDB = Depends(get_current_user)):
    return db.query(models.Dier).where(models.Dier.soort == soort).limit(limit).offset(offset).all()


@app.get("/dier/{dier_id}", status_code=status.HTTP_200_OK)
async def get_dier_by_id(dier_id: int, db: db_dependency):
    return db.query(models.Dier).where(models.Dier.dier_id == dier_id).first()


@app.get("/random", status_code=status.HTTP_200_OK)
async def get_random(db: db_dependency, soort: int):
    alle_dieren = await get_alle_dieren(db, soort)
    dieren_count = len(alle_dieren)
    offset = r.choice(range(0, dieren_count))
    return {"offset": offset, "length": dieren_count}


@app.post('/reservering/', status_code=status.HTTP_201_CREATED)
async def maak_reservering(reservering: ReserveringBase, db: db_dependency,
                           current_user: UserInDB = Depends(get_current_user)):
    db_reservering = models.Reservering(**reservering.dict())
    db.add(db_reservering)
    db.commit()
    db.refresh(db_reservering)
    return db_reservering


@app.get('/reserveringen', status_code=status.HTTP_200_OK)
async def get_reserveringen(db: db_dependency, current_user: UserInDB = Depends(get_current_user)):
    return db.query(models.Reservering).where(models.Reservering.gebruiker_id == current_user.gebruiker_id).all()


@app.delete('/reservering/{reservering_id}', status_code=status.HTTP_200_OK)
async def delete_reservering(reservering_id: int, db: db_dependency,  current_user: UserInDB = Depends(get_current_user)):
    db.query(models.Reservering).where(models.Reservering.reservering_id == reservering_id).delete()
    db.commit()
    return {"message": "reservering verwijderd"}
