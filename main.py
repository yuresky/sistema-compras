from funcoes_sistema import *
import json
import os

os.system('cls')

#menu 1.0
import sys

lista_cadastro_clientes = []
lista_cadastro_produtos = []

def menu():
    print("======= Menu =======")
    print("1. Cadastrar")
    print("2. Cadastrar produto")
    print("3. Editar informações")
    print("3. Remover")
    print("4. Pesquisar")
    print("5. Listar")
    print("6. Gerar relatório")
    print("7. Sair do programa")
    print("====================")

opcao = 0
while opcao != 7:
    menu()
    escolha = int(input("Informe qual será a operação: "))  # Converta a entrada para um número inteiro

    if escolha == 1:
        cadastro_cliente(lista_cadastro_clientes)
    
    elif escolha == 2:
        cadastro_produto(lista_cadastro_produtos)

    elif escolha == 3:
        editar_cliente()
    
    elif escolha == 7:
        sys.exit()  # sair do programa

# Resto do código



#cadastrar_cliente()

#Função que busca
# with open("clientes.json","r") as arquivo:
#     dados = json.load(arquivo)
    
#     for cliente in dados:
#         print(cliente['Nome'])


    # Obter informações do novo cliente

# with open ("clientes.json", "r") as arquivo:
#     clientes = json.load(arquivo)
#     for cliente in clientes:
#         nome = cliente["ID"]
#         print (nome)