from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uvicorn

from src import database, models
from src.routes import router  # Import the router from your routes module

engine = create_engine(database.DATABASE_URL)
models.Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

database.create_predefined_exercises(SessionLocal())

app = FastAPI()

# Include the router in your main FastAPI app
app.include_router(router)


def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, access_log=False)


if __name__ == "__main__":
    main()
