import yaml

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import uuid

import src.models.exercise
import src.models.user
from src import models

DATABASE_URL = "sqlite:///./exercise_tracker.db"

engine = create_engine(DATABASE_URL)
models.Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_user(db: Session) -> src.models.user.User:
    user_uuid = uuid.uuid4()
    new_user = src.models.user.User(id=user_uuid)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def create_workout(db: Session, workout: src.models.exercise.Workout):
    db_workout = src.models.exercise.Workout(**workout.dict())
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout


def create_exercise(db: Session, exercise: src.models.exercise.Exercise):
    db_exercise = src.models.exercise.Exercise(**exercise.dict())
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise


def create_predefined_exercises(db: Session):
    with open('src/exercises.yaml', 'r') as f:
        predefined_exercises = yaml.safe_load(f)

    for exercise in predefined_exercises:
        db_exercise = src.models.exercise.PredefinedExercise(**exercise)
        db.add(db_exercise)
    db.commit()


def get_predefined_exercises(db: Session, workout_type: str):
    return db.query(src.models.exercise.PredefinedExercise).filter(
        src.models.exercise.PredefinedExercise.workout_type == workout_type).all()

