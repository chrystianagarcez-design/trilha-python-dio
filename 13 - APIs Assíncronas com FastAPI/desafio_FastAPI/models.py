from sqlalchemy import Column, Integer, String, Date, Numeric, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "cliente"

    cpf_cnpj = Column(String, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    endereco = Column(String, nullable=False)

    contas = relationship("Conta", back_populates="cliente")


class Agencia(Base):
    __tablename__ = "agencia"

    cod_agencia = Column(Integer, primary_key=True, autoincrement=True)
    nome_agencia = Column(String, nullable=False)

    contas = relationship("Conta", back_populates="agencia")
    historicos = relationship("HistoricoConta", back_populates="agencia")


class Conta(Base):
    __tablename__ = "conta"

    id_conta = Column(Integer, primary_key=True, autoincrement=True)
    cod_agencia = Column(Integer, ForeignKey("agencia.cod_agencia"), nullable=False)
    numero_conta = Column(Integer, nullable=False, index=True)
    cpf_cnpj = Column(String, ForeignKey("cliente.cpf_cnpj"), nullable=False)
    valor_saldo = Column(Numeric(10, 2), nullable=False, default=0.00)
    valor_limite = Column(Numeric(10, 2), nullable=False, default=0.00)

    cliente = relationship("Cliente", back_populates="contas")
    agencia = relationship("Agencia", back_populates="contas")
    historicos = relationship("HistoricoConta", back_populates="conta")


class HistoricoConta(Base):
    __tablename__ = "historico_conta"

    id_historico_conta = Column(Integer, primary_key=True, autoincrement=True)
    cod_agencia = Column(Integer, ForeignKey("agencia.cod_agencia"), nullable=False)
    id_conta = Column(Integer, ForeignKey("conta.id_conta"), nullable=False)
    flag_tipo_debito = Column(Boolean, nullable=False)
    flag_tipo_credito = Column(Boolean, nullable=False)
    valor_transacao = Column(Numeric(10, 2), nullable=False)
    data_transacao = Column(DateTime, nullable=False)

    agencia = relationship("Agencia", back_populates="historicos")
    conta = relationship("Conta", back_populates="historicos")