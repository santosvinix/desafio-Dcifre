from fastapi import FastAPI
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey 
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Carregar o .env
load_dotenv()

print(os.getenv('DB_USUARIO'), os.getenv('DB_SENHA'), os.getenv('DB_HOST'), os.getenv('DB_NOME'))

# Criando o banco de dados 'empresas' em MySQL
db = create_engine(f"mysql+pymysql://{os.getenv('DB_USUARIO')}:{os.getenv('DB_SENHA')}@{os.getenv('DB_HOST')}:3306/{os.getenv('DB_NOME')}.db")
Session = sessionmaker(bind=db)
session = Session()

# Criando as tabelas
Base = declarative_base()
Base.metadata.create_all(bind=db)



# Utilizando o FastAPI
app = FastAPI()


@app.get("/")
def home():
    return "Minha api está no ar"