from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.models import Base


class Workout(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True)
    workout_type = Column(String)
    date = Column(String)
    exercises = relationship("Exercise", back_populates="workout")


class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True)
    workout_id = Column(Integer, ForeignKey('workouts.id'))
    exercise_type = Column(String)
    reps = Column(Integer)
    sets = Column(Integer)
    weight = Column(Integer)
    pr_flag = Column(Integer)
    workout = relationship("Workout", back_populates="exercises")


class PredefinedExercise(Base):
    __tablename__ = 'predefined_exercises'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    min_reps = Column(Integer)
    max_reps = Column(Integer)
    workout_type = Column(String)
