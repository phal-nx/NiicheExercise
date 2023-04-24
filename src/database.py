import yaml

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

import uuid
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


def create_user(db: Session) -> models.User:
    user_uuid = uuid.uuid4()
    new_user = models.User(id=user_uuid)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def create_workout(db: Session, workout: models.Workout):
    db_workout = models.Workout(**workout.dict())
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout


def create_exercise(db: Session, exercise: models.Exercise):
    db_exercise = models.Exercise(**exercise.dict())
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise


def create_predefined_exercises(db: Session):
    with open('exercises.yaml', 'r') as f:
        predefined_exercises = yaml.safe_load(f)

    for exercise in predefined_exercises:
        db_exercise = models.PredefinedExercise(**exercise)
        db.add(db_exercise)
    db.commit()


def get_predefined_exercises(db: Session, workout_type: str):
    return db.query(models.PredefinedExercise).filter(models.PredefinedExercise.workout_type == workout_type).all()

