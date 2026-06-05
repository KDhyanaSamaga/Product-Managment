from fastapi import FastAPI
from database import Base,SessionLocal,get_db,engine

app =FastAPI()
# Base.metadata.create_all(engine)
