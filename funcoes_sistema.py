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


        preco = input("Informe o preço do produto: ").strip()

        while not preco.replace('.', '', 1).isdigit():
            print("Preço inválido! O preço deve ser um número decimal.")
            preco = input("Informe o preço do produto: ").strip()

        preco = float(preco)



  
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
        email = input("Informe o email do cliente: ").title()
        email = email if email else "Não informado pelo(a) cliente"

        while not telefone.strip() or telefone.isalpha():
            telefone = input("Informe o telefone do cliente: ")
        #Corrigir o problema do valor float

  
        # O sistema cria a formatação para armazenar a informação do produto no arquivo json
        with open("clientes.json", "r") as arquivo:
            identificador = json.load(arquivo)
        cliente = {'ID': len(identificador)+1, 'Nome': nome, 'Telefone': f"+55 {telefone}", 'E-mail': email}
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
        

def cadastrar_compra():
    while True:
        produtos = []
        clientes = []
        compras = []

        with open("produtos.json", "r", encoding="utf-8") as arquivo:
            produtos = json.load(arquivo)

        with open("clientes.json", "r", encoding="utf-8") as arquivo:
            clientes = json.load(arquivo)

        with open("compras.json", "r", encoding="utf-8") as arquivo:
            compras = json.load(arquivo)

        print('\nInformações dos Clientes: \n ----------------------------------\n')
        for x in clientes:
        
            print (f'ID: {x["ID"]}\nNome: {x["Nome"]}\nTelefone: {x["Telefone"]}\nE-mail: {x["E-mail"]}')
            print("\n-----------------------------------\n")

        cliente_encontrado = False
        cliente_selecionado = None

        while not cliente_encontrado:
            codigo_cliente = input("Informe o código do cliente: ")

            if not codigo_cliente.isdigit() or codigo_cliente.isspace():
                print("Código do cliente inválido. Digite novamente.")
                continue

            for cliente in clientes:
                if cliente['ID'] == int(codigo_cliente):
                    cliente_encontrado = True
                    cliente_selecionado = cliente
                    break

        print('\nInformações dos produtos: \n ----------------------------------\n')
        for x in compras:
        
            print (f'ID: {x["ID"]}\nNome: {x["Nome"]}\nDescrição: {x["Descrição"]}\nPreço: {x["Preço"]}')
            print("\n-----------------------------------\n")


        produtos_comprados = []

        while True:
            codigo_produto = input("Informe o código do produto (ou 'sair' para encerrar a compra): ")

            if codigo_produto == 'sair':
                break


            if not codigo_produto.isdigit() or codigo_produto.isspace():
                print("Código do produto inválido. Digite novamente.")
                continue

            produto_encontrado = False
            produto_selecionado = None

            for produto in produtos:
                if produto['ID'] == int(codigo_produto):
                    produto_encontrado = True
                    produto_selecionado = produto
                    print(f"Você adicionou {produto['Nome']} na sua lista de compras!")
                    break

            if not produto_encontrado:
                print("Produto não encontrado.")
                continue

            produtos_comprados.append(produto_selecionado['ID'])

        forma_pagamento = input("Informe a forma de pagamento (PIX, dinheiro ou cartão): ").title()
        if forma_pagamento not in ["Pix", "Dinheiro", "Cartão"]:
            print("Forma de pagamento inválida! Verifique se digitou corretamente.")
            continue
        
        while True:
            data = input("Informe a data da compra no formato (dia/mês/ano): ")
            def verificar_data(data):
                partes_data = data.split('/')
                if len(partes_data) != 3:
                    return False

                dia, mes, ano = partes_data

                if not dia.isdigit() or not mes.isdigit() or not ano.isdigit():
                    return False

                dia = int(dia)
                mes = int(mes)
                ano = int(ano)

                if not (1 <= dia <= 31) or not (1 <= mes <= 12) or not (2000 <= ano <= 99999999):
                    return False

                return True

            if verificar_data(data):
                break
            else:
                print("Data inválida!")
                continue

        valor_total = 0.0

        for produto_id in produtos_comprados:
            for produto in produtos:
                if produto['ID'] == produto_id:
                    valor_total += float(produto['Preço'])
                    break

        compra = {
            'ID': len(compras) + 1,
            'ID Cliente': cliente_selecionado['ID'],
            'Nome do cliente': cliente_selecionado['Nome'],
            'Forma de pagamento': forma_pagamento,
            'Data': data,
            'Valor Total': valor_total,
            'Produtos comprados': produtos_comprados
        }

        with open("compras.json", "w", encoding="utf-8") as arquivo:
            compras.append(compra)
            json.dump(compras, arquivo, indent=4)

        print("Compra cadastrada com sucesso!")

        loop = input("Você quer continuar cadastrando novas compras? [S/N]").upper()
        if loop == "N":
            break

    input("Digite algo para voltar ao menu: ")




def editar_compras():
    # Abrir o arquivo JSON e carregar os dados dos clientes
    with open("compras.json", "r") as arquivo:
        compras = json.load(arquivo)
    
    # Exibir a lista de clientes para o usuário selecionar qual deseja editar
    print("Lista de compras:")
    for compra in compras:
        print(f"ID: {compra['ID']}, Nome do cliente: {compra['Nome do cliente']}, Forma de pagamento: {compra['Forma de pagamento']}, Valor total: {compra['Valor Total']}")
    
    # Solicitar ao usuário o ID do cliente que deseja editar
    id_compra = int(input("Digite o ID da compra que deseja editar: "))
    
    # Procurar o cliente com base no ID fornecido
    compra_encontrada = None
    for compra in compras:
        if compra['ID'] == id_compra:
            compra_encontrada = compra
            break
    
    # Verificar se o cliente foi encontrado
    if compra_encontrada:
        # Solicitar ao usuário as novas informações para editar o cliente
        novo_nome = input("Digite o novo nome do cliente (ou deixe em branco para manter o valor atual): ")
        nova_data = input("Digite a nova data da compra (ou deixe em branco para manter o valor atual): ")
        nova_forma_pag = input("Digite a nova forma de pagamento (ou deixe em branco para manter o valor atual): ")
        
        # Atualizar as informações do cliente apenas se valores válidos foram fornecidos
        if novo_nome:
            compra_encontrada['Nome do cliente'] = novo_nome
        if nova_data:
            compra_encontrada['Data'] = nova_data
        if nova_forma_pag:
            compra_encontrada['Forma de pagamento'] = nova_forma_pag
        

        # Salvar as alterações no arquivo JSON
        with open("compras.json", "w") as arquivo:
            json.dump(compras, arquivo, indent=4)
        
        print("Compras atualizada com sucesso!")
    else:
        print("Compra não encontrada.")
    input("Digite alguma coisa para voltar ao menú: ")


def listar_compras():
    with open('compras.json', encoding="utf-8") as arquivo:
        informacoes= json.load(arquivo)
        
        print('\nInformações das compras: \n ----------------------------------\n')
        for x in informacoes:
        
            print (f'ID: {x["ID"]}\nID do Cliente: {x["ID Cliente"]}\nNome do Cliente: {x["Nome do cliente"]}\nForma de Pagamento: {x["Forma de pagamento"]}\nData: {x["Data"]}\nValor: {x["Valor Total"]}\nID dos Produtos Comprados: {x["Produtos comprados"]}')
            print("\n-----------------------------------\n")
    input("Digite algo para voltar ao menú: ")


def excluir_compra():
    with open("clientes.json", "r") as arquivo:
        clientes = json.load(arquivo)

    for cliente in clientes:
        print(f"ID: {cliente['ID']}, Nome: {cliente['Nome']}")

    valor_cliente = int(input("Informe o ID do cliente: "))

    cliente_encontrado = False
    for cliente in clientes:
        if cliente["ID"] == valor_cliente:
            cliente_encontrado = True
            compras = cliente.get("compras", [])
            if compras:
                print("Compras do cliente:")
                for compra in compras:
                    print(f"ID: {compra['ID']}, Descrição: {compra['Descrição']}")
                
                valor_compra = int(input("Informe o ID da compra que você deseja excluir: "))
                compras = [compra for compra in compras if compra["ID"] != valor_compra]

                cliente["compras"] = compras
                with open("clientes.json", "w") as arquivo:
                    json.dump(clientes, arquivo, indent=4)
                
                print(f"Compra com ID {valor_compra} do cliente com ID {valor_cliente} excluída com sucesso!")
            else:
                print("O cliente não possui compras.")
            break

    if not cliente_encontrado:
        print("Cliente não encontrado!")

    input("Digite algo para voltar ao menu: ")

def relatorio ():
    with open('produtos.json','r'), ("compras.json","r") as arquivo:
        produtos= json.load(arquivo)
    with open ("compras.json") as arquivo:
        compras = json.load(arquivo)
    with open ("clientes.json") as arquivo:
        clientes = json.load(arquivo)
    