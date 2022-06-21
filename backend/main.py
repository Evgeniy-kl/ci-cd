from typing import List

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import api
import model
from database import SessionLocal, engine
from schema import UserItem

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/items/", response_model=List[UserItem])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = api.get_items(db, skip=skip, limit=limit)
    return items


@app.post("/users/", response_model=UserItem)
def create_user(user: UserItem, db: Session = Depends(get_db)):
    return api.create_user(db=db, user=user)


if __name__ == "__main__":
    model.Base.metadata.create_all(bind=engine)
    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)
