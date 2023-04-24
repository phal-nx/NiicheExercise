from sqlalchemy import Column, String

from src.models import Base


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
