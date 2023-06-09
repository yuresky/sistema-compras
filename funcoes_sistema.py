import json

def cadastro_produto():
    while True:
        produtos = []
        nome = ""
        preco = ""
        #Enquanto o nome não for adequado, o programa vai pedir o nome
        while not nome.strip() or nome.isdigit() or len(nome.strip()) == 1 or len(nome.replace(" ", "")) < 3:
            nome = input("Informe o nome do produto: ").title()


        # O programa pede a descrição e oo preço do produto respectivamente, se caso a descrição não seja informada, o sistema deve adotar essa expressão: "Não informado pelo(a) cliente"
        descricao = input("Informe a descrição do produto: ").title()
        descricao = descricao if descricao else "Não informado pelo(a) cliente"

        while not preco.strip() or preco.isalpha():
            preco = input("Informe o preço do produto: ")
        #Corrigir o problema do valor float

  
        # O sistema cria a formatação para armazenar a informação do produto no arquivo json
        with open("produtos.json", "r") as arquivo:
            identificador = json.load(arquivo)
        produto = {'ID': len(identificador)+1, 'Nome': nome, 'Descrição': descricao, 'Preço': preco}
        produtos.append(produto)  # Adicionar o produto à lista de produtos da iteração atual

        # O sistema abre o arquivo json
        with open("produtos.json", "r") as arquivo:
            conteudo_atual = json.load(arquivo)
        
        # O sistema estende a lista conteudo_atual com os produtos da iteração atual
        conteudo_atual.extend(produtos)

        with open("produtos.json", "w") as arquivo:
            json.dump(conteudo_atual, arquivo, indent=4)

        print("Produto cadastrado com sucesso!")

        loop = input("Você quer continuar cadastrando novos produtos? [S/N]").upper()
        if loop == "N":
            break
        
    input("Digite alguma coisa para voltar ao menu: ")
    

def cadastro_cliente():
    while True:
        clientes = []
        nome = ""
        telefone = ""
        #Enquanto o nome não for adequado, o programa vai pedir o nome
        while not nome.strip() or nome.isdigit() or len(nome.strip()) == 1 or len(nome.replace(" ", "")) < 3:
            nome = input("Informe o nome do cliente: ").title()


        # O programa pede a descrição e oo preço do produto respectivamente, se caso a descrição não seja informada, o sistema deve adotar essa expressão: "Não informado pelo(a) cliente"
        email = input("Informe a descrição do produto: ").title()
        email = email if email else "Não informado pelo(a) cliente"

        while not telefone.strip() or telefone.isalpha():
            telefone = input("Informe o preço do produto: ")
        #Corrigir o problema do valor float

  
        # O sistema cria a formatação para armazenar a informação do produto no arquivo json
        with open("clientes.json", "r") as arquivo:
            identificador = json.load(arquivo)
        cliente = {'ID': len(identificador)+1, 'Nome': nome, 'Telefone': telefone, 'E-mail': email}
        clientes.append(cliente)  # Adicionar o produto à lista de produtos da iteração atual

        # O sistema abre o arquivo json
        with open("clientes.json", "r") as arquivo:
            conteudo_atual = json.load(arquivo)
        
        # O sistema estende a lista conteudo_atual com os produtos da iteração atual
        conteudo_atual.extend(clientes)

        with open("clientes.json", "w") as arquivo:
            json.dump(conteudo_atual, arquivo, indent=4)

        print("Cliente cadastrado com sucesso!")

        loop = input("Você quer continuar cadastrando novos clientes? [S/N]").upper()
        if loop == "N":
            break
        
    input("Digite alguma coisa para voltar ao menu: ")







def busca_cliente():
    #Função que busca clientes por nome
    with open("clientes.json","r") as arquivo:
        dados = json.load(arquivo)
        clientes = [cliente['Nome'] for cliente in dados]
        print(clientes)
        while True:
            busca = input('Qual é o cliente que você está procurando mais informações? ').lower().strip()
            resultados = [cliente for cliente in dados if busca in cliente['Nome'].lower()]

            if resultados:
                for resultado in resultados:
                    print(f"Encontramos o(a) cliente {(busca).title()}\n {resultado}")
                break
            else:
                print("Não encontrado(a), talvez você tenha buscado por:.")
        input("Digite alguma coisa para ir até ao menú")


def editar_cliente():
    # Abrir o arquivo JSON e carregar os dados dos clientes
    with open("clientes.json", "r") as arquivo:
        clientes = json.load(arquivo)
    
    # Exibir a lista de clientes para o usuário selecionar qual deseja editar
    print("Lista de clientes:")
    for cliente in clientes:
        print(f"ID: {cliente['ID']}, Nome: {cliente['Nome']}")
    
    # Solicitar ao usuário o ID do cliente que deseja editar
    id_cliente = int(input("Digite o ID do cliente que deseja editar: "))
    
    # Procurar o cliente com base no ID fornecido
    cliente_encontrado = None
    for cliente in clientes:
        if cliente['ID'] == id_cliente:
            cliente_encontrado = cliente
            break
    
    # Verificar se o cliente foi encontrado
    if cliente_encontrado:
        # Solicitar ao usuário as novas informações para editar o cliente
        novo_nome = input("Digite o novo nome do cliente (ou deixe em branco para manter o valor atual): ")
        novo_telefone = input("Digite o novo telefone do cliente (ou deixe em branco para manter o valor atual): ")
        novo_email = input("Digite o novo e-mail do cliente (ou deixe em branco para manter o valor atual): ")
        
        # Atualizar as informações do cliente apenas se valores válidos foram fornecidos
        if novo_nome:
            cliente_encontrado['Nome'] = novo_nome
        if novo_telefone:
            cliente_encontrado['Telefone'] = novo_telefone
        if novo_email:
            cliente_encontrado['E-mail'] = novo_email
        

        # Salvar as alterações no arquivo JSON
        with open("clientes.json", "w") as arquivo:
            json.dump(clientes, arquivo, indent=4)
        
        print("Cliente atualizado com sucesso!")
    else:
        print("Cliente não encontrado.")
    input("Digite alguma coisa para voltar ao menú: ")



def editar_produto():
    # Abrir o arquivo JSON e carregar os dados dos clientes
    with open("produtos.json", "r") as arquivo:
        produtos = json.load(arquivo)
    
    # Exibir a lista de clientes para o usuário selecionar qual deseja editar
    print("Lista de clientes:")
    for produto in produtos:
        print(f"ID: {produto['ID']}, Nome: {produto['Nome']}")
    
    # Solicitar ao usuário o ID do cliente que deseja editar
    id_produto = int(input("Digite o ID do produto que deseja editar: "))
    
    # Procurar o cliente com base no ID fornecido
    produto_encontrado = None
    for produto in produtos:
        if produto['ID'] == id_produto:
            cliente_encontrado = produto
            break
    
    # Verificar se o cliente foi encontrado
    if produto_encontrado:
        # Solicitar ao usuário as novas informações para editar o cliente
        novo_nome = input("Digite o novo nome do produto (ou deixe em branco para manter o valor atual): ")
        nova_descricao = input("Digite a nova descrição do produto (ou deixe em branco para manter o valor atual): ")
        novo_preco = input("Digite o novo e-preço do produto (ou deixe em branco para manter o valor atual): ")
        
        # Atualizar as informações do cliente apenas se valores válidos foram fornecidos
        if novo_nome:
            cliente_encontrado['Nome'] = novo_nome
        if nova_descricao:
            cliente_encontrado['Telefone'] = nova_descricao
        if novo_preco:
            cliente_encontrado['E-mail'] = novo_preco
        

        # Salvar as alterações no arquivo JSON
        with open("clientes.json", "w") as arquivo:
            json.dump(produtos, arquivo, indent=4)
        
        print("Cliente atualizado com sucesso!")
    else:
        print("Cliente não encontrado.")
    input("Digite alguma coisa para voltar ao menú: ")



def excluir_produto():
    with open("clientes.json", "r") as arquivo:
        produtos = json.load(arquivo)

    for produto in produtos:
        print(f"ID: {produto['ID']}, Nome: {produto['Nome']}")

    valor = int(input("Informe o ID do produto que você quer excluir: "))

    novos_produtos = [produto for produto in produtos if produto["ID"] != valor]

    if len(novos_produtos) < len(produtos):
        with open("produtos.json", "w") as arquivo:
            json.dump(novos_produtos, arquivo, indent=4)
        print(f"Cliente com ID {valor} excluído com sucesso!")
    else:
        print("Cliente não encontrado!")

    input("Digite algo para voltar ao menú: ") #Colocar a função de valores correspondentes
        
def excluir_cliente():
    with open("clientes.json", "r") as arquivo:
        clientes = json.load(arquivo)

    for cliente in clientes:
        print(f"ID: {cliente['ID']}, Nome: {cliente['Nome']}")

    valor = int(input("Informe o ID da pessoa que você quer excluir: "))

    novos_clientes = [cliente for cliente in clientes if cliente["ID"] != valor]

    if len(novos_clientes) < len(clientes):
        with open("clientes.json", "w") as arquivo:
            json.dump(novos_clientes, arquivo, indent=4)
        print(f"Cliente com ID {valor} excluído com sucesso!")
    else:
        print("Cliente não encontrado!")

    input("Digite algo para voltar ao menú: ") #Colocar a função de valores correspondentes
    

def listar_clientes():
    with open('clientes.json') as arquivo:
        informacoes= json.load(arquivo)
        
        print('\nInformações dos Clientes: \n ----------------------------------\n')
        for x in informacoes:
        
            print (f'ID: {x["ID"]}\nNome: {x["Nome"]}\nTelefone: {x["Telefone"]}\nE-mail: {x["E-mail"]}')
            print("\n-----------------------------------\n")
    input("Digite algo para voltar ao menú: ")

def listar_produtos():
    with open('produtos.json', encoding="utf-8") as arquivo:
        informacoes= json.load(arquivo)
        
        print('\nInformações dos produtos: \n ----------------------------------\n')
        for x in informacoes:
        
            print (f'ID: {x["ID"]}\nNome: {x["Nome"]}\nDescrição: {x["Descrição"]}\nPreço: {x["Preço"]}')
            print("\n-----------------------------------\n")
    input("Digite algo para voltar ao menú: ")


def realizar_compra():
    with open ("produtos.json","r", encoding="utf-8") as arquivo:
        produtos = json.load(arquivo)
    with open ("clientes.json", "r") as arquivo:
        clientes = json.load(arquivo)
    for cliente in clientes:
        print(f"ID: {cliente['ID']}, Nome: {cliente['Nome']}")

    codigo_cliente = int(input("Informe o código do cliente: "))
    cliente_encontrado = False
    for cliente in clientes:
        if cliente['ID'] == codigo_cliente:
            cliente_encontrado = True
            break
    
    if not cliente_encontrado:
        print("Cliente não encontrado.")
        return
    
    while True:
        for produto in produtos:
            print(f"ID: {produto['ID']}, Nome: {produto['Nome']}, Preço: {produto['Preço']}")

        codigo_produto = int(input("Informe o código do produto (ou 'sair' para encerrar a compra): "))
        if codigo_produto == 'sair':
            break
        
        produto_encontrado = False
        for produto in produtos:
            if produto['ID'] == codigo_produto:
                produto_encontrado = True
                break
        
        if not produto_encontrado:
            print("Produto não encontrado.")
            continue
        
        itens_compra.append(produto)
        valor_total += produto['preco']

    forma_pagamento = input("Informe a forma de pagamento (PIX, dinheiro ou cartão): ")
    data = input("Informe a data da compra: ")
    
    valor_total = 0.0
    itens_compra = []
    
    compra = {'Cliente': cliente, 'Forma de Pagamento': forma_pagamento, 'Data': data, 'Valor Total': valor_total, 'Itens': itens_compra}
    
    with open("compras.json", "a") as arquivo:
        arquivo.write(json.dumps(compra) + "\n")
    
    print("Compra realizada com sucesso!")

def exibir_compras():
    with open("compras.json", "r") as arquivo:
        compras = arquivo.readlines()
    
    if not compras:
        print("Nenhuma compra registrada.")
    else:
        for compra in compras:
            compra = json.loads(compra)
            print("Cliente:", compra['Cliente']['Nome'])
            print("Forma de Pagamento:", compra['Forma de Pagamento'])
            print("Data:", compra['Data'])
            print("Valor Total:", compra['Valor Total'])
            print("Itens da Compra:")
            for item in compra['Itens']:
                print(" -", item['Nome'])
            print("---------------------------------------")
        