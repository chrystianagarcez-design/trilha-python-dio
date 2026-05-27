from pydantic import BaseModel, ConfigDict
from datetime import date, datetime
from decimal import Decimal

# --- SCHEMAS DE CLIENTE ---
class ClienteBase(BaseModel):
    cpf_cnpj: str
    nome: str
    data_nascimento: date
    endereco: str

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    model_config = ConfigDict(from_attributes=True)


# --- SCHEMAS DE AGENCIA ---
class AgenciaBase(BaseModel):
    nome_agencia: str

class AgenciaCreate(AgenciaBase):
    pass

class AgenciaResponse(AgenciaBase):
    cod_agencia: int
    model_config = ConfigDict(from_attributes=True)


# --- SCHEMAS DE CONTA ---
class ContaBase(BaseModel):
    cod_agencia: int
    numero_conta: int
    cpf_cnpj: str
    valor_saldo: Decimal = Decimal("0.00")
    valor_limite: Decimal = Decimal("0.00")

class ContaCreate(ContaBase):
    pass

class ContaResponse(ContaBase):
    id_conta: int
    model_config = ConfigDict(from_attributes=True)


# --- SCHEMAS DE HISTORICO ---
class HistoricoContaBase(BaseModel):
    cod_agencia: int
    id_conta: int
    flag_tipo_debito: bool
    flag_tipo_credito: bool
    valor_transacao: Decimal
    data_transacao: datetime

class HistoricoContaCreate(HistoricoContaBase):
    pass

class HistoricoContaResponse(HistoricoContaBase):
    id_historico_conta: int
    model_config = ConfigDict(from_attributes=True)