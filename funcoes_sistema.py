import json
# def cadastro_cliente (): 
#     lista = []
#     valores = input("Informe o seu nome, telefone e e-mail, respectivamente (separando por vírgula): ").split(",")
#     lista.append({'nome': valores[0], 'telefone': valores[1], 'e-mail': valores[2]})
#     with open("clientes.txt", "r+") as arquivo:
#         arquivo.writelines([f"{dados['nome']}, {dados['telefone']},{dados['e-mail']}, \n" for dados in lista])

#Cadastro
# def cadastro_cliente(lista):
#     contador =[]
#     nome = ""
#     while not nome:
#         nome = input("Informe o seu nome: ")

#     telefone = int(input("Informe o seu telefone: "))
#     telefone = telefone if telefone else "Não informado pelo(a) cliente"
#     email = input("informe o seu e-mail: ")
#     email = email if email else "Não informado pelo(a) cliente"

#     lista.append({'nome': nome, 'telefone': telefone, 'e-mail': email})
#     contador.append({'nome': nome, 'telefone': telefone, 'e-mail': email})

#     novo_id = len(lista)

#     with open("clientes.txt", "a") as arquivo:
#         arquivo.writelines([f"\nID: {novo_id}\nNome: {dados['nome']}\nTelefone: {dados['telefone']}\nE-mail: {dados['e-mail']}\n" for dados in contador])
        
#     print("Cliente cadastrado com sucesso!")
#     input("Digite alguma coisa para voltar ao menú: ")

import json

def cadastro_produto(lista):
    nome = ""
    while not nome:
        nome = input("Informe o nome do produto: ")

    descricao = input("Informe a descrição do produto: ")
    descricao = descricao if descricao else "Não informado pelo(a) cliente"
    preco = input("Informe o preço do produto: ")

    with open("produtos.json", "r") as arquivo:
        identificador = json.load(arquivo)
    produto = {'ID': len(identificador)+1, 'Nome': nome, 'Descrição': descricao, 'Preço': preco}
    lista.append(produto)

    with open("produtos.json", "r") as arquivo:
        conteudo_atual = json.load(arquivo)

    conteudo_atual.extend(lista)

    with open("produtos.json", "w") as arquivo:
        json.dump(conteudo_atual, arquivo, indent=4)

    print("Cliente cadastrado com sucesso!")
    input("Digite alguma coisa para voltar ao menu: ")
    


def cadastro_cliente(lista):
    nome = ""
    while not nome:
        nome = input("Informe o seu nome: ")

    telefone = input("Informe o seu telefone: ")
    telefone = telefone if telefone else "Não informado pelo(a) cliente"
    email = input("Informe o seu e-mail: ")
    email = email if email else "Não informado pelo(a) cliente"

    with open("produtos.json", "r") as arquivo:
        identificador = json.load(arquivo)
    cliente = {'ID': len(identificador)+1, 'Nome': nome, 'Telefone': telefone, 'E-mail': email}
    lista.append(cliente)

    with open("produtos.json", "r") as arquivo:
        conteudo_atual = json.load(arquivo)

    conteudo_atual.extend(lista)

    with open("produtos.json", "w") as arquivo:
        json.dump(conteudo_atual, arquivo, indent=4)

    print("Cliente cadastrado com sucesso!")
    input("Digite alguma coisa para voltar ao menu: ")


def editar_cliente():
    with open ("clientes.json","r") as arquivo:
        print (json.load(arquivo))