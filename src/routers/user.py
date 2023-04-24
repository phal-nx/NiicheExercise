from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

import src.models.user
from src import schemas
from src.database import get_db
from src.routers.exercise import exercise_router
from fastapi import APIRouter

user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@exercise_router.post("/", response_model=schemas.User, tags=["users"])
def create_user(db: Session = Depends(get_db)):
    db_user = create_user(db)
    return db_user


@exercise_router.get("/{user_id}", response_model=schemas.User, tags=["users"])
def get_user(user_id: str, db: Session = Depends(get_db)):
    db_user = db.query(src.models.user.User).filter(src.models.user.User.id == user_id).first()
    if db_user:
        return db_user
    else:
        raise HTTPException(status_code=404, detail="User not found")
