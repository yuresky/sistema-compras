from funcoes_sistema import *
import os
import sys

os.system('cls')

def menu():
    print("======= Menu =======")
    print("1. Cadastrar")
    print("2. Editar informações")
    print("3. Remover")
    print("4. Pesquisar")
    print("5. Listar")
    print("6. Gerar relatório")
    print("7. Sair do programa")
    print("====================")

opcao = ''
while opcao != "7":
    menu()
    escolha = input("Informe qual será a operação: ")  # Converta a entrada para um número inteiro

    if escolha == "1":
        while True:
            print("=====================")
            print("1. Cadastrar Cliente")
            print("2. Cadastrar Produto")
            print("3. Cadastrar Compra")
            print("4. Voltar")
            print("=====================")
            
            escolha_cadastro = input("Informe qual será a operação: ")
            if escolha_cadastro == "1":
                cadastro_cliente()
            elif escolha_cadastro == "2":
                cadastro_produto()
            elif escolha_cadastro == "3":
                cadastrar_compra()
            elif escolha_cadastro == "4":
                break
            else:
                print("Opção inválida!")
                continue

    elif escolha == "2":
        while True:
            print("=====================")
            print("1. Editar informações do Cliente")
            print("2. Editar informações do Produto")
            print("3. Editar informações da Compra")
            print("4. Voltar")
            print("=====================")

            escolha_edicao = input("Informe qual será a operação: ")

            if escolha_edicao == "1":
                editar_cliente()
            elif escolha_edicao == "2":
                editar_produto()
            elif escolha_edicao == "3":
                editar_compras()
            elif escolha_edicao == "4":
                break
            else:
                print("Opção inválida!")
                continue

    elif escolha == "3":
        while True:
            print("=====================")
            print("1. Remover Cliente")
            print("2. Remover Produto")
            print("3. Remover Compra")
            print("4. Voltar")
            print("=====================")

            escolha_remocao = input("Informe qual será a operação: ")

            if escolha_remocao == "1":
                excluir_cliente()
            elif escolha_remocao == "2":
                excluir_produto()
            elif escolha_remocao == "3":
                excluir_compra()
            elif escolha_remocao == "4":
                break
            else:
                print("Opção inválida!")
                continue

    elif escolha == "4":
        while True:
            print("=====================")
            print("1. Pesquisar Cliente")
            print("2. Pesquisar Produto")
            print("3. Pesquisar Compra")
            print("4. Voltar")
            print("=====================")

            escolha_pesquisa = input("Informe qual será a operação: ")

            if escolha_pesquisa == "1":
                pesquisar_cliente()
            elif escolha_pesquisa == "2":
                pesquisar_produtos()
            elif escolha_pesquisa == "3":
                pesquisar_compra()
            elif escolha_pesquisa == "4":
                break
            else:
                print("Opção inválida!")
                continue

    elif escolha == "5":
        while True:
            print("=====================")
            print("1. Listar Clientes")
            print("2. Listar Produtos")
            print("3. Listar Compras")
            print("4. Voltar")
            print("=====================")

            escolha_listagem = input("Informe qual será a operação: ")

            if escolha_listagem == "1":
                listar_clientes()
            elif escolha_listagem == "2":
                listar_produtos()
            elif escolha_listagem == "3":
                while True:
                    print("=====================")
                    print("1. Listar Todas as Compras")
                    print("2. Listar Compras por Data")
                    print("3. Listar Compras por Forma de Pagamento")
                    print("4. Voltar")
                    print("=====================")
                    escolha_compras = input("Informe qual será a operação: ")

                    if escolha_compras == "1":
                        listar_compras()
                    elif escolha_compras == "2":
                        listar_comprasdata()
                    elif escolha_compras == "3":
                        listar_compraspag()
                    elif escolha_compras == "4":
                        break  # Sai do loop interno e retorna ao loop principal
                    else:
                        print("Opção inválida!")
                        continue
            elif escolha_listagem == "4":
                break
            else:
                print("Opção inválida!")
                continue


    elif escolha == "6":
        relatorio()
        
    elif escolha == "7":
        print("Saindo do programa...")
        sys.exit()  # sair do programa

    else:
        print("Opção inválida!")