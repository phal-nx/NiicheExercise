from fastapi import FastAPI, Depends, HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from typing import List

from src import database, models, schemas
from src.database import get_db

import uuid

from fastapi import APIRouter

router = APIRouter()


@router.post("/users/", response_model=schemas.User)
def create_user(db: Session = Depends(get_db)):
    db_user = create_user(db)
    return db_user


@router.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: str, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        return db_user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@router.get("/exercises/{exercise_id}", response_model=schemas.Exercise)
def get_exercise(exercise_id: str, db: Session = Depends(get_db)):
    db_exercise = db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()
    if db_exercise:
        return db_exercise
    else:
        raise HTTPException(status_code=404, detail="Exercise not found")


@router.get("/exercises/", response_model=schemas.Exercise)
def get_exercise(db: Session = Depends(get_db)):
    db_exercise = db.query(models.Exercise).filter()
    if db_exercise:
        return db_exercise
    else:
        raise HTTPException(status_code=404, detail="No exercises found")


@router.get("/predefined_exercises/", response_model=List[schemas.PredefinedExercise])
def get_exercise(db: Session = Depends(get_db)):
    db_exercises = db.query(models.PredefinedExercise).all()
    breakpoint()
    return db_exercises


@router.get("/exercises/user/{user_id}", response_model=List[schemas.Exercise])
def get_exercises_for_user(user_id: str, db: Session = Depends(get_db)):
    user_exercises = db.query(models.Exercise).filter(models.Exercise.user_id == user_id).all()
    return user_exercises


@router.post("/workouts/", response_model=schemas.WorkoutCreate)
def create_workout_route(workout: schemas.WorkoutCreate, db: Session = Depends(database.get_db)):
    return database.create_workout(db, workout)


@router.post("/exercises/", response_model=schemas.ExerciseCreate)
def create_exercise_route(exercise: schemas.Exercise, db: Session = Depends(database.get_db)):
    return database.create_exercise(db, exercise)

