import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

cnx = sqlite3.connect(ROOT_PATH / 'desafio_FastAPI.db')
cursor = cnx.cursor()

def criar_tabelas():
    cursor.execute('''CREATE TABLE IF NOT EXISTS cliente (
        cpf_cnpj TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        data_nascimento date NOT NULL,
        endereco TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS agencia (
        cod_agencia INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_agencia TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS conta (
        id_conta INTEGER PRIMARY KEY AUTOINCREMENT,
        cod_agencia INTEGER NOT NULL,
        numero_conta INTEGER NOT NULL,
        cpf_cnpj TEXT NOT NULL,
        valor_saldo DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
        valor_limite DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
        FOREIGN KEY (cod_agencia) REFERENCES agencia (cod_agencia),
        FOREIGN KEY (cpf_cnpj) REFERENCES cliente (cpf_cnpj)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS historico_conta (
        id_historico_conta INTEGER PRIMARY KEY AUTOINCREMENT,
        cod_agencia INTEGER NOT NULL,
        numero_conta INTEGER NOT NULL,
        flag_tipo_debito BOOLEAN NOT NULL,
        flag_tipo_credito BOOLEAN NOT NULL,
        valor_transacao DECIMAL(10, 2) NOT NULL,
        data_transacao DATETIME NOT NULL,
        FOREIGN KEY (cod_agencia) REFERENCES agencia (cod_agencia),
        FOREIGN KEY (numero_conta) REFERENCES conta (numero_conta)
    )''')

    cnx.commit()

def inserir_cliente(cpf_cnpj, nome, data_nascimento, endereco):
    cursor.execute('''INSERT INTO cliente (cpf_cnpj, nome, data_nascimento, endereco) 
                      VALUES (?, ?, ?, ?)''', (cpf_cnpj, nome, data_nascimento, endereco))
    cnx.commit()

def inserir_agencia(nome_agencia):
    cursor.execute('''INSERT INTO agencia (nome_agencia) 
                      VALUES (?)''', (nome_agencia,))
    cnx.commit()

def inserir_conta(cod_agencia, numero_conta, cpf_cnpj, valor_saldo, valor_limite):
    cursor.execute('''INSERT INTO conta (cod_agencia, numero_conta, cpf_cnpj, valor_saldo, valor_limite)
                      VALUES (?, ?, ?, ?, ?)''', (cod_agencia, numero_conta, cpf_cnpj, valor_saldo, valor_limite))
    cnx.commit()

def inserir_historico_conta(cod_agencia, numero_conta, flag_tipo_debito, flag_tipo_credito, valor_transacao, data_transacao):
    cursor.execute('''INSERT INTO historico_conta (cod_agencia, numero_conta, flag_tipo_debito, flag_tipo_credito, valor_transacao, data_transacao) 
                      VALUES (?, ?, ?, ?, ?, ?)''', (cod_agencia, numero_conta, flag_tipo_debito, flag_tipo_credito, valor_transacao, data_transacao))
    cnx.commit()

def buscar_cliente(cpf_cnpj):
    cursor.execute('''SELECT * FROM cliente WHERE cpf_cnpj = ?''', (cpf_cnpj))
    return cursor.fetchone()

def buscar_agencia(cod_agencia):
    cursor.execute('''SELECT * FROM agencia WHERE cod_agencia = ?''', (cod_agencia))
    return cursor.fetchone()

def buscar_conta(numero_conta):
    cursor.execute('''SELECT * FROM conta WHERE numero_conta = ?''', (numero_conta))
    return cursor.fetchone()

def buscar_historico_conta(numero_conta):
    cursor.execute('''SELECT * FROM historico_conta WHERE numero_conta = ?''', (numero_conta))
    return cursor.fetchall()

def atualizar_saldo_conta(numero_conta, novo_saldo):
    cursor.execute('''UPDATE conta SET valor_saldo = ? WHERE numero_conta = ?''', (novo_saldo, numero_conta))
    cnx.commit()

def atualizar_limite_conta(numero_conta, novo_limite):
    cursor.execute('''UPDATE conta SET valor_limite = ? WHERE numero_conta = ?''', (novo_limite, numero_conta))
    cnx.commit()

# cria as tabelas caso nao existam
criar_tabelas()