from abc import ABC, abstractmethod
import datetime
import os
import subprocess
import random

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass
    
class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self._transacoes.append({"transacao": transacao, "_valor": transacao._valor, "_data": datetime.datetime.now()})

    def __str__(self):
        if not self._transacoes:
            return "Historico vazio."
        
        details = [f"  - {t['transacao'].__class__.__name__} de R$ {t['_valor']:.2f} na data/hora {t['_data']}." for t in self._transacoes]
        return "Historico de Transacoes:\n" + "\n".join(details)
    
class Conta:
    def __init__(self, cliente: Cliente, numero: int, agencia: str = "0001"):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

        cliente.adicionar_conta(self)

    @staticmethod
    def nova_conta(cliente: Cliente, numero: int):
        return Conta(cliente, numero)

    def saldo(self) -> float:
        return self._saldo

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("Valor invalido.")
            return False
        
        if self._saldo < valor:
            print("Saldo insuficiente.")
            return False

        self._saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        return True

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print("Valor invalido.")
            return False

        self._saldo += valor
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso.")
        return True

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def __str__(self):
        return f"Cliente {self._cliente._nome if hasattr(self._cliente, '_nome') else 'Cliente inexistente.'}, Agencia: {self._agencia}, Numero: {self._numero}, Saldo: R$ {self._saldo:.2f}, Limite: R$ {self._limite:.2f}" if hasattr(self, '_limite') else f"Cliente {self._cliente._nome if hasattr(self._cliente, '_nome') else 'Cliente inexistente.'}, Agencia: {self._agencia}, Numero: {self._numero}, Saldo: R$ {self._saldo:.2f}" 
    
class Cliente:
    def __init__(self, cpf=None, nome=None, data_nascimento=None, endereco=None):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._endereco = endereco
        self._contas = []
 
    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def realizar_transacao(self, conta, transacao: Transacao):
        if conta in self._contas:
            transacao.registrar(conta)
        else:
            print(f"Conta {conta._numero} nao pertence a este cliente.")

class ContaCorrente(Conta):
    def __init__(self, cliente: Cliente, numero: int, agencia: str = "0001", limite: float = 1000.0, limite_saques: int = 4):
        super().__init__(cliente, numero, agencia)
        self._limite = limite
        self._limite_saques = limite_saques
        self._saques_realizados_hoje = 0

    def sacar(self, valor: float) -> bool:
        saldo_disponivel = self._saldo + self._limite

        if valor <= 0:
            print("Valor invalido.")
            return False
        if valor > saldo_disponivel:
            print("Saldo e limite insuficientes")
            return False
        if self._saques_realizados_hoje >= self._limite_saques:
            print("Limite de saques diarios excedido.")
            return False

        self._saldo -= valor
        self._saques_realizados_hoje += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso (incluindo limite: R$ {self._limite:.2f}).")
        return True

    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques

class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    def registrar(self, conta: Conta):
        if conta.depositar(self._valor):
            conta.historico.adicionar_transacao(self)
            return True
        return False

class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    def registrar(self, conta: Conta):
        if conta.sacar(self._valor):
            conta.historico.adicionar_transacao(self)
            return True
        return False

# funcionalidades por opcao selecionada
def menu(opcao_menu):
    if opcao_menu == 1:
        valor_deposito = float(input("Valor do deposito: "))
        deposito = Deposito(valor_deposito)
        cliente.realizar_transacao(conta1, deposito)
        
        opcao_menu = int(input("\nOpção desejada: "))
        menu(opcao_menu)

    if opcao_menu == 2:
        valor_saque = float(input("Valor do saque: "))
        
        saque = Saque(valor_saque)
        cliente.realizar_transacao(conta1, saque)

        opcao_menu = int(input("\nOpção desejada: "))
        menu(opcao_menu)

    if opcao_menu == 3:
        print(conta1)

        opcao_menu = int(input("\nOpção desejada: "))
        menu(opcao_menu)

    if opcao_menu == 4:
        print(conta1.historico)

        opcao_menu = int(input("\nOpção desejada: "))
        menu(opcao_menu)

    if opcao_menu == 5:
        valor_deposito = float(input("Valor do deposito: "))
        deposito = Deposito(valor_deposito)
        cliente.realizar_transacao(conta2, deposito)
        
        opcao_menu = int(input("\nOpção desejada: "))
        menu(opcao_menu)

    if opcao_menu == 6:
        valor_saque = float(input("Valor do saque: "))
        
        saque = Saque(valor_saque)
        cliente.realizar_transacao(conta2, saque)

        opcao_menu = int(input("\nOpção desejada: "))
        menu(opcao_menu)

    if opcao_menu == 7:
        print(conta2)

        opcao_menu = int(input("\nOpção desejada: "))
        menu(opcao_menu)

    if opcao_menu == 8:
        print(conta2.historico)

        opcao_menu = int(input("\nOpção desejada: "))
        menu(opcao_menu)

    if opcao_menu == 0:
        exit()

class PessoaFisica(Cliente):
    def __init__(self, endereco: str, cpf: str, nome: str, data_nascimento: datetime.date):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf
    
if __name__ == "__main__":
    # limpar o console
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

    # dados iniciais do cliente
    cpf = input("Informe seu CPF: ")
    nome = input("Informe seu nome: ")
    data_nascimento = input("Informe sua data de nascimento: ")
    endereco = input("Informe seu endereço: ")

    # cria duas contas para o cliente
    cliente = PessoaFisica(endereco=endereco, cpf=cpf, nome=nome, data_nascimento=data_nascimento)
    conta1 = Conta(cliente=cliente, numero=random.randint(100000, 199999))
    conta2 = ContaCorrente(cliente=cliente, numero=random.randint(200000, 299999))

    # exibe contas criadas
    print(f"\nContas criadas:")
    for conta in cliente._contas:
        print(conta)

    # exibe menu de opcoes para as duas contas criadas
    print(f"""
        ============= MENU =============
        [1] - Depositar conta {conta1.numero}
        [2] - Sacar conta {conta1.numero}
        [3] - Exibir saldo conta {conta1.numero}
        [4] - Exibir historico conta {conta1.numero}

        [5] - Depositar conta {conta2.numero}
        [6] - Sacar conta {conta2.numero}
        [7] - Exibir saldo conta {conta2.numero}
        [8] - Exibir historico conta {conta2.numero}

        [0] - Sair
        ================================
    """)

    opcao_menu = int(input("Opção desejada: "))

    if opcao_menu <= -1 or opcao_menu > 8:
        print ("Opção inválida! ")
        pause = input("Pressione Enter para continuar...")
    else:
        menu(opcao_menu)