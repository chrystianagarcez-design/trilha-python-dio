import httpx
import json

from rich import print
from rich.console import Console
from rich.panel import Panel

import os
import subprocess
import random

# URL da aplicacao FastAPI
BASE_URL = "http://127.0.0.1:8000"

console = Console()

def status_api_bancaria_assincrona_com_fastapi():

    console.print("\nVerificando status do servidor...", style="bold blue")

    # API FastAPI online
    status_api = httpx.get(f"{BASE_URL}/status")
    console.print(Panel(str(status_api), title="Status da API Bancária Assíncrona com FastAPI", subtitle="GET /status", expand=False))
    console.print(f"{json.dumps(status_api.json(), indent=4, ensure_ascii=False)}")

    # # Exemplo de ENVIO via POST
    # console.print("\nEnviando dados para a API...", style="bold green")
    # dados = {
    #     "nome": "Automação Metis",
    #     "descricao": "Tarefa executada via console"
    # }
    # response_post = httpx.post(f"{BASE_URL}/enviar-dados", json=dados)
    
    # if response_post.status_code == 200:
    #     console.print(f"Sucesso: {response_post.json()['mensagem']}", style="bold green")
    # else:
    #     console.print(f"Erro ao enviar: {response_post.status_code}", style="bold red")

def gera_token_jwt():
    console.print("\nGerando token para autenticação...", style="bold magenta")
    console.print(Panel(str("teste"), title="Token de autenticação", subtitle="POST /token", expand=False))
    # Simulação de geração de token JWT (substitua por lógica real de autenticação)

# funcionalidades por opcao selecionada
def menu(opcao_menu):
    if opcao_menu == 1:
        # exibe contas criadas
        print(f"\nContas criadas:")
        for conta in [conta1, conta2]:
            print(conta)        

        # exibe menu de opcoes para as duas contas criadas
        exibe_menu()        

        opcao_menu = int(input("\nOpção desejada: "))
        menu(opcao_menu)

    # if opcao_menu == 1:
    #     valor_deposito = float(input("Valor do deposito: "))
    #     deposito = Deposito(valor_deposito)
    #     cliente.realizar_transacao(conta1, deposito)
        
    #     opcao_menu = int(input("\nOpção desejada: "))
    #     menu(opcao_menu)

    # if opcao_menu == 2:
    #     valor_saque = float(input("Valor do saque: "))
        
    #     saque = Saque(valor_saque)
    #     cliente.realizar_transacao(conta1, saque)

    #     opcao_menu = int(input("\nOpção desejada: "))
    #     menu(opcao_menu)

    # if opcao_menu == 3:
    #     print(conta1)

    #     opcao_menu = int(input("\nOpção desejada: "))
    #     menu(opcao_menu)

    # if opcao_menu == 4:
    #     print(conta1.historico)

    #     opcao_menu = int(input("\nOpção desejada: "))
    #     menu(opcao_menu)

    # if opcao_menu == 5:
    #     valor_deposito = float(input("Valor do deposito: "))
    #     deposito = Deposito(valor_deposito)
    #     cliente.realizar_transacao(conta2, deposito)
        
    #     opcao_menu = int(input("\nOpção desejada: "))
    #     menu(opcao_menu)

    # if opcao_menu == 6:
    #     valor_saque = float(input("Valor do saque: "))
        
    #     saque = Saque(valor_saque)
    #     cliente.realizar_transacao(conta2, saque)

    #     opcao_menu = int(input("\nOpção desejada: "))
    #     menu(opcao_menu)

    # if opcao_menu == 7:
    #     print(conta2)

    #     opcao_menu = int(input("\nOpção desejada: "))
    #     menu(opcao_menu)

    # if opcao_menu == 8:
    #     print(conta2.historico)

    #     opcao_menu = int(input("\nOpção desejada: "))
    #     menu(opcao_menu)

    if opcao_menu == 0:
        exit()

    if opcao_menu <= -1 or opcao_menu > 8:
        print ("Opção inválida! ")
        pause = input("Pressione Enter para continuar...")

        # exibe menu de opcoes para as duas contas criadas
        exibe_menu()        

        opcao_menu = int(input("\nOpção desejada: "))
        menu(opcao_menu)

def exibe_menu():
    print(f"""
        ============= MENU =============
        [1] - Depositar conta {conta1['numero']}
        [2] - Sacar conta {conta1['numero']}
        [3] - Exibir saldo conta {conta1['numero']}
        [4] - Exibir historico conta {conta1['numero']}

        [5] - Depositar conta {conta2['numero']}
        [6] - Sacar conta {conta2['numero']}
        [7] - Exibir saldo conta {conta2['numero']}
        [8] - Exibir historico conta {conta2['numero']}

        [0] - Sair
        ================================
    """)

if __name__ == "__main__":

    # limpar o console
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

    status_api_bancaria_assincrona_com_fastapi()
    gera_token_jwt()

    # dados iniciais do cliente
    cpf = input("\nInforme seu CPF: ")
    nome = input("Informe seu nome: ")
    data_nascimento = input("Informe sua data de nascimento: ")
    endereco = input("Informe seu endereço: ")

    # cria duas contas para o cliente
    pessoa = {"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}
    conta1 = {**pessoa, "agencia": "0001", "numero": random.randint(100000, 199999)}
    conta2 = {**pessoa, "agencia": "0001", "numero": random.randint(200000, 299999)}

    # exibe contas criadas
    print(f"\nContas criadas:")
    for conta in [conta1, conta2]:
        print(conta)

    # exibe menu de opcoes para as duas contas criadas
    exibe_menu()

    opcao_menu = int(input("Opção desejada: "))

    while opcao_menu <= -1 or opcao_menu > 8:
        print ("Opção inválida! ")
        pause = input("Pressione Enter para continuar...")

        opcao_menu = int(input("\nOpção desejada: "))
    else:
        menu(opcao_menu)
