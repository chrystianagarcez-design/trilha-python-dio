from fastapi import FastAPI
from contextlib import asynccontextmanager
import sqlalchemy
import databases

metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine("sqlite:///desafio_FastAPI.db", connect_args={"check_same_thread": False})
database = databases.Database("sqlite:///desafio_FastAPI.db")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    metadata.create_all(engine)
    # await gera_token_jwt()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

@app.get("/status")
def status_api():
    return {"message": "Desafio: API Bancária Assíncrona com FastAPI **** ONLINE ! ****"}

# gerar token JWT para cadastrar uma parte da chave na base com o objetivo de registrar a "autenticacao" de uma transacao de deposito e/ou saque