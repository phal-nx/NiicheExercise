from pydantic import BaseModel
from typing import Optional


class BaseModelApp(BaseModel):
    class Config:
        orm_mode = True


# Auth schema
class User(BaseModelApp):
    id: str
    email: str
    password: str


# Exercise schemas
class WorkoutCreate(BaseModelApp):
    workout_type: str
    date: str


class ExerciseCreate(BaseModelApp):
    workout_id: int
    exercise_type: str
    reps: int
    sets: int
    weight: int
    pr_flag: Optional[int] = None


class Exercise(BaseModelApp):
    workout_id: int
    exercise_type: str
    reps: int
    sets: int
    weight: int
    pr_flag: Optional[int] = None


class PredefinedExercise(BaseModelApp):
    name: str
    min_reps: int
    max_reps: int
    workout_type: str
