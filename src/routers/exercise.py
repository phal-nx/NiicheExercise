from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import src.models.exercise
from src import database

from fastapi import APIRouter


from src import schemas
from src.database import get_db

exercise_router = APIRouter(
    # prefix="/items",
    tags=["Exercise"],
)


@exercise_router.get("/exercises/{exercise_id}", response_model=schemas.Exercise)
def get_exercise(exercise_id: str, db: Session = Depends(get_db)):
    db_exercise = db.query(src.models.exercise.Exercise).filter(src.models.exercise.Exercise.id == exercise_id).first()
    if db_exercise:
        return db_exercise
    else:
        raise HTTPException(status_code=404, detail="Exercise not found")

@exercise_router.post("/exercises/", response_model=schemas.ExerciseCreate, tags=["exercise"])
def create_exercise_route(exercise: schemas.Exercise, db: Session = Depends(database.get_db)):
    return database.create_exercise(db, exercise)


@exercise_router.get("/predefined_exercises/", response_model=List[schemas.PredefinedExercise], tags=["exercise"])
def get_exercise(db: Session = Depends(get_db)):
    db_exercises = db.query(src.models.exercise.PredefinedExercise).all()
    return db_exercises


@exercise_router.get("/exercises/user/{user_id}", response_model=List[schemas.Exercise], tags=["exercise"])
def get_exercises_for_user(user_id: str, db: Session = Depends(get_db)):
    user_exercises = db.query(src.models.exercise.Exercise).filter(
        src.models.exercise.Exercise.user_id == user_id).all()
    return user_exercises


@exercise_router.post("/workouts/", response_model=schemas.WorkoutCreate, tags=["exercise"])
def create_workout_route(workout: schemas.WorkoutCreate, db: Session = Depends(database.get_db)):
    return database.create_workout(db, workout)




