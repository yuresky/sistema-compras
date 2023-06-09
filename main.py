from funcoes_sistema import *
import os

os.system('cls')

#menu 1.0
import sys

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
        cadastro_cliente()
    
    elif escolha == 2:
        cadastro_produto()

    elif escolha == 3:
        editar_cliente()
    
    elif escolha == 4:
        busca_cliente()

    elif escolha == 5:
        busca_cliente()
    
    elif escolha == 6:
        editar_cliente()
    
    elif escolha == 7:
        excluir_cliente()
        
    elif escolha == 8:
        listar_clientes()
    
    elif escolha == 9:
        listar_produtos()

    elif escolha == 10:
        realizar_compra()

    elif escolha == 11:
        exibir_compras()


    elif escolha == 12:
        sys.exit()  # sair do programa

# Resto do código



#cadastrar_cliente()


# with open ("clientes.json", "r") as arquivo:
#     clientes = json.load(arquivo)
#     for cliente in clientes:
#         nome = cliente["ID"]
#         print (nome)

