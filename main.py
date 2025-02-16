from fastapi import FastAPI
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey 
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()


@app.get("/")
def home():
    return "Minha api está no ar"