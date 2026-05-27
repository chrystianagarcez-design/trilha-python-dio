from sqlalchemy.orm import Session
from . import models, schemas

class ClienteService:
    @staticmethod
    def get_by_id(db: Session, cpf_cnpj: str):
        return db.query(models.Cliente).filter(models.Cliente.cpf_cnpj == cpf_cnpj).first()

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Cliente).offset(skip).limit(limit).all()

    @staticmethod
    def create(db: Session, cliente: schemas.ClienteCreate):
        db_cliente = models.Cliente(**cliente.model_dump())
        db.add(db_cliente)
        db.commit()
        db.refresh(db_cliente)
        return db_cliente


class AgenciaService:
    @staticmethod
    def get_by_id(db: Session, cod_agencia: int):
        return db.query(models.Agencia).filter(models.Agencia.cod_agencia == cod_agencia).first()

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Agencia).offset(skip).limit(limit).all()

    @staticmethod
    def create(db: Session, agencia: schemas.AgenciaCreate):
        db_agencia = models.Agencia(**agencia.model_dump())
        db.add(db_agencia)
        db.commit()
        db.refresh(db_agencia)
        return db_agencia


class ContaService:
    @staticmethod
    def get_by_id(db: Session, id_conta: int):
        return db.query(models.Conta).filter(models.Conta.id_conta == id_conta).first()

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Conta).offset(skip).limit(limit).all()

    @staticmethod
    def create(db: Session, conta: schemas.ContaCreate):
        db_conta = models.Conta(**conta.model_dump())
        db.add(db_conta)
        db.commit()
        db.refresh(db_conta)
        return db_conta


class HistoricoContaService:
    @staticmethod
    def get_by_id(db: Session, id_historico_conta: int):
        return db.query(models.HistoricoConta).filter(models.HistoricoConta.id_historico_conta == id_historico_conta).first()

    @staticmethod
    def get_by_conta(db: Session, id_conta: int):
        return db.query(models.HistoricoConta).filter(models.HistoricoConta.id_conta == id_conta).all()

    @staticmethod
    def create(db: Session, historico: schemas.HistoricoContaCreate):
        db_historico = models.HistoricoConta(**historico.model_dump())
        db.add(db_historico)
        db.commit()
        db.refresh(db_historico)
        return db_historico