from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from . import schemas, services
from main import database, metadata, engine

# Dependência simulada para pegar a sessão do banco (substitua pela sua configuração real de database)
def get_db():
    db = database.connect()
    try:
        yield db
    finally:
        pass  # db.close()

router = APIRouter()

# --- ENDPOINTS CLIENTE ---
@router.post("/clientes/", response_model=schemas.ClienteResponse, status_code=status.HTTP_201_CREATED)
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = services.ClienteService.get_by_id(db, cpf_cnpj=cliente.cpf_cnpj)
    if db_cliente:
        raise HTTPException(status_code=400, detail="CPF/CNPJ já cadastrado")
    return services.ClienteService.create(db=db, cliente=cliente)

@router.get("/clientes/", response_model=List[schemas.ClienteResponse])
def read_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.ClienteService.get_all(db, skip=skip, limit=limit)


# --- ENDPOINTS AGENCIA ---
@router.post("/agencias/", response_model=schemas.AgenciaResponse, status_code=status.HTTP_201_CREATED)
def create_agencia(agencia: schemas.AgenciaCreate, db: Session = Depends(get_db)):
    return services.AgenciaService.create(db=db, agencia=agencia)

@router.get("/agencias/", response_model=List[schemas.AgenciaResponse])
def read_agencias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.AgenciaService.get_all(db, skip=skip, limit=limit)


# --- ENDPOINTS CONTA ---
@router.post("/contas/", response_model=schemas.ContaResponse, status_code=status.HTTP_201_CREATED)
def create_conta(conta: schemas.ContaCreate, db: Session = Depends(get_db)):
    # Valida se cliente existe
    if not services.ClienteService.get_by_id(db, conta.cpf_cnpj):
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    # Valida se agencia existe
    if not services.AgenciaService.get_by_id(db, conta.cod_agencia):
        raise HTTPException(status_code=404, detail="Agência não encontrada")
    return services.ContaService.create(db=db, conta=conta)

@router.get("/contas/", response_model=List[schemas.ContaResponse])
def read_contas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.ContaService.get_all(db, skip=skip, limit=limit)


# --- ENDPOINTS HISTORICO ---
@router.post("/historicos/", response_model=schemas.HistoricoContaResponse, status_code=status.HTTP_201_CREATED)
def create_historico(historico: schemas.HistoricoContaCreate, db: Session = Depends(get_db)):
    if not services.ContaService.get_by_id(db, historico.id_conta):
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return services.HistoricoContaService.create(db=db, historico=historico)

@router.get("/historicos/conta/{id_conta}", response_model=List[schemas.HistoricoContaResponse])
def read_historico_da_conta(id_conta: int, db: Session = Depends(get_db)):
    return services.HistoricoContaService.get_by_conta(db, id_conta=id_conta)