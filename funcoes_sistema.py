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

        #O sistema pergunta se o usuário quer continuar cadastrando
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

def editar_cliente():
    # Abrir o arquivo JSON e carregar os dados dos clientes
    with open("clientes.json", "r") as arquivo:
        clientes = json.load(arquivo)
    with open("compras.json","r") as arquivo:
        compras = json.load(arquivo)
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
        novo_nome = ""
        novo_telefone = ""
        while not novo_nome.strip() or novo_nome.isdigit() or len(novo_nome.strip()) == 1 or len(novo_nome.replace(" ", "")) < 3:
            novo_nome = input(f"Digite o novo nome do cliente (ou digite o atual nome):\nNome atual: {cliente['Nome']}\n: ").title()

        while not novo_telefone.strip() or novo_telefone.isalpha():
            novo_telefone = input(f"Digite o novo telefone do cliente (ou digite o número atual)\nNúmero atual: {cliente['Telefone']}\n: ")

        novo_email = input("Digite o novo e-mail do cliente (ou deixe em branco para manter o valor atual): ")
        
        # Atualizar as informações do cliente apenas se valores válidos foram fornecidos
        if novo_nome:
                cliente_encontrado['Nome'] = novo_nome
                # Atualizar também o nome do cliente no arquivo "compras.json"
                for compra in compras:
                    if compra['ID Cliente'] == cliente_encontrado['ID']:
                        compra['Nome do cliente'] = novo_nome
        if novo_telefone:
            cliente_encontrado['Telefone'] = novo_telefone
        if novo_email:
            cliente_encontrado['E-mail'] = novo_email
        

        # Salvar as alterações no arquivo JSON
        with open("clientes.json", "w") as arquivo:
            json.dump(clientes, arquivo, indent=4)

        with open("compras.json", "w") as arquivo:
            json.dump(compras, arquivo, indent=4)
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
        novo_nome = ""
        novo_preco = ""
        while not novo_nome.strip() or novo_nome.isdigit() or len(novo_nome.strip()) == 1 or len(novo_nome.replace(" ", "")) < 3:
            novo_nome = input(f"Digite o novo nome do produto (ou digite o nome atual para não modificar)\nNome atual: {produto['Nome']}\n: ").title()

        nova_descricao = input("Digite a nova descrição do produto (ou deixe em branco para manter o valor atual): ")

        while not novo_preco.strip() or novo_preco.isalpha():
            novo_preco = input("Digite o novo preço do produto (ou digite o preço antigo)\nPreço antigo: {produto['Preço']}\n: ")
        
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


def excluir_compras_clientes(cliente_id):
    #Abre o arquivo compras.json
    with open("compras.json", "r") as arquivo:
        compras = json.load(arquivo)

    #List comprehseion! novas_compras recebe os valores de compra que tiverem o valor do id cliente diferente do que o usuário informou.
    novas_compras = [compra for compra in compras if compra["ID Cliente"] != cliente_id]

    #Aqui ele verifica se de fato ocorreu a exclusão do dado verificando o tamnho das duas listas.
    if len(novas_compras) < len(compras):
        with open("compras.json", "w") as arquivo:
            json.dump(novas_compras, arquivo, indent=4)
        print(f"Todas as compras do cliente com ID {cliente_id} foram excluídas.")
    else:
        print(f"Cliente com ID {cliente_id} não encontrado.")

def excluir_produto():
    #Abre o arquivo produtos.json
    with open("produtos.json", "r") as arquivo:
        produtos = json.load(arquivo)

    #Para cada produto em produtos
    for produto in produtos:
        print(f"ID: {produto['ID']}, Nome: {produto['Nome']}")

    valor = int(input("Informe o ID do produto que você quer excluir: "))

    #Abre o arquivo compras.json
    with open("compras.json", "r") as arquivo:
        compras = json.load(arquivo)

    #Para cada compra em compras
    for compra in compras:
        if valor in compra["Produtos comprados"]:
            compra["Produtos comprados"].remove(valor)

    #List comprehseion! novos_produtos recebe os valores de produto que tiverem o valor do id produto diferente do que o usuário informou.
    novos_produtos = [produto for produto in produtos if produto["ID"] != valor]

    if len(novos_produtos) < len(produtos):
        with open("produtos.json", "w") as arquivo:
            json.dump(novos_produtos, arquivo, indent=4)
        print(f"Produto com ID {valor} excluído com sucesso!")
    else:
        print("Produto não encontrado!")

    input("Digite algo para voltar ao menu: ")

def excluir_cliente():
    with open("clientes.json", "r") as arquivo:
        clientes = json.load(arquivo)

    for cliente in clientes:
        print(f"ID: {cliente['ID']}, Nome: {cliente['Nome']}")

    valor = int(input("Informe o ID da pessoa que você quer excluir: "))

    excluir_compras_clientes(valor)  # Chama a função para remover as compras do cliente

    #List comprehseion! novos_clientes recebe os valores de cliente que tiverem o valor do id cliente diferente do que o usuário informou.
    novos_clientes = [cliente for cliente in clientes if cliente["ID"] != valor]

    if len(novos_clientes) < len(clientes):
        with open("clientes.json", "w") as arquivo:
            json.dump(novos_clientes, arquivo, indent=4)
        print(f"Cliente com ID {valor} excluído com sucesso!")
    else:
        print("Cliente não encontrado!")

    input("Digite algo para voltar ao menu: ")
 #Colocar a função de valores correspondentes
    

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
        for x in produtos:
        
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

        while True:
            forma_pagamento = input("Informe a forma de pagamento (PIX, dinheiro ou cartão): ").title()
            if forma_pagamento not in ["Pix", "Dinheiro", "Cartão"]:
                print("Forma de pagamento inválida! Verifique se digitou corretamente.")
                continue
            break

        while True:
            data = input("Informe a data da compra no formato (dia/mês/ano)\nOBS: Ano anterior a 2000 NÃO É VÁLIDO!\n: ")
            verificar_data(data)
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
        print(f'O Total a pagar é {valor_total}')

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
    # Abrir o arquivo JSON e carregar os dados das compras e clientes
    with open("compras.json", "r") as arquivo:
        compras = json.load(arquivo)

    with open("clientes.json","r") as arquivo:
        clientes = json.load(arquivo)
    
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
        novo_nome = ""
        nova_forma_pag = ""
        while not novo_nome.strip() or novo_nome.isdigit() or len(novo_nome.strip()) == 1 or len(novo_nome.replace(" ", "")) < 3:
            novo_nome = input(f"Digite o novo nome do cliente (ou digite o nome antigo para manter o valor atual)\nNome antigo: {compra_encontrada['Nome do cliente']}: ").title()
        
        while True:
            nova_data = input(f"Informe a nova data da compra no formato (dia/mês/ano)\nOBS: Ano anterior a 2000 NÃO É VÁLIDO!\nCaso não queira mudar a data, repita a seguinte data {compra_encontrada['Data']}\n: ")
            verificar_data(nova_data)
            if verificar_data(nova_data):
                break

            else:
                print("Data inválida!")
                continue

        while True:
            nova_forma_pag = input(f"Digite a nova forma de pagamento (ou digite a forma de pagamento anterior para não modificar)\nForma de pagamento anterior: {compra_encontrada['Forma de pagamento']}\n: ").title()
            if nova_forma_pag not in ["Pix", "Dinheiro", "Cartão"]:
                print("Forma de pagamento inválida! Verifique se digitou corretamente.")
                continue
            break
        
        # Atualizar as informações do cliente apenas se valores válidos foram fornecidos
            # Atualizar as informações da compra apenas se valores válidos foram fornecidos
        if novo_nome:
            compra_encontrada['Nome do cliente'] = novo_nome
            # Atualizar também o nome do cliente no arquivo "clientes.json"
            for cliente in clientes:
                if cliente['ID'] == compra_encontrada['ID Cliente']:
                    cliente['Nome'] = novo_nome
                    break

        if nova_data:
            compra_encontrada['Data'] = nova_data
        if nova_forma_pag:
            compra_encontrada['Forma de pagamento'] = nova_forma_pag

        
        # Salvar as alterações no arquivo JSON
        with open("compras.json", "w") as arquivo:
            json.dump(compras, arquivo, indent=4)
        with open("clientes.json","w") as arquivo:
            json.dump(clientes, arquivo, indent=4)
        
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

def relatorio():
    with open('produtos.json', 'r') as arquivo:
        produtos = json.load(arquivo)
    with open('compras.json') as arquivo:
        compras = json.load(arquivo)
    with open('clientes.json') as arquivo:
        clientes = json.load(arquivo)

    def tot_compras():
        contador = 0
        print('-------------')
        print('RELATÓRIO:')
        print('-------------\n')
        print('______________________')
        print('Quantidade de Compras:')
        for i in compras:
            contador += 1
        return contador

    def tot_clientes():
        contador = 0
        print('_______________________')
        print('Quantidade de clientes:')
        for i in clientes:
            contador += 1
        return contador


    def tot_produtos():
        contador = 0
        print('_______________________')
        print('Quantidade de produtos:')
        for i in produtos:
            contador += 1
        return contador   

    def tot_compras_por_cliente():
        contador_por_cliente = {}
        print('_______________________________')
        print('Total de compras por cliente: ')
        for compra in compras:
            id_cliente = compra['ID Cliente']
            contador_por_cliente[id_cliente] = contador_por_cliente.get(id_cliente, 0) + 1
        for cliente in clientes:
            id_cliente = cliente['ID']
            nome_cliente = cliente['Nome']
            total_compras = contador_por_cliente.get(id_cliente, 0)
            print('-----------------------------------------------------------')
            print(f"Cliente: {nome_cliente}, Total de compras: {total_compras}")
            print('-----------------------------------------------------------')
        return None

    def tot_compras_por_produto():
        contador_por_produto = {}
        print('_______________________________')
        print('Total de compras por produto:\n')
        for compra in compras:
            produto_comprado = compra['ID Cliente']
            contador_por_produto[produto_comprado] = contador_por_produto.get(produto_comprado, 0) + 1
        for produto in produtos:
            produto_comprado = produto['ID']
            nome_produto = produto['Nome']
            total_produtos_comprados = contador_por_produto.get(produto_comprado, 0)
            print('-----------------------------------------------------------')
            print(f"Cliente: {nome_produto}, Total de compras: {total_produtos_comprados}")
            print('-----------------------------------------------------------')
        return None

    def tot_compras_por_forma_pagamento():
        contador_por_forma_pagamento = {}
        print('__________________________________________')
        print('Total de compras por forma de pagamento:')
        for compra in compras:
            forma_pagamento = compra['Forma de pagamento']
            contador_por_forma_pagamento[forma_pagamento] = contador_por_forma_pagamento.get(forma_pagamento, 0) + 1
        for forma_pagamento in contador_por_forma_pagamento:
            total_compras = contador_por_forma_pagamento[forma_pagamento]
            print('-----------------------------------------------------------')
            print(f"Forma de pagamento: {forma_pagamento}, Total de compras: {total_compras}")
            print('-----------------------------------------------------------')
        return None

    def somatorio_compras():
        total = 0
        print('________________________________')
        print('Somatório de todas as compras:')
        for compra in compras:
            valor_total = compra['Valor Total']
            total += valor_total
        print(f"Total: {total}\n")
        return None

    # Imprimir o relatório no terminal
    print(f"Total de compras: {tot_compras()}\n")
    print(f"Total de clientes: {tot_clientes()}\n")
    print(f"Total de produtos: {tot_produtos()}\n")
    tot_compras_por_cliente()
    tot_compras_por_produto()
    tot_compras_por_forma_pagamento()
    somatorio_compras()
    input("Digite algo para voltar ao menú: ")

def pesquisar_cliente():
    with open("clientes.json", "r") as arquivo:
        clientes = json.load(arquivo)


    entrada = input("Informe o ID ou o nome do cliente: ")

    for cliente in clientes:
        if str(cliente["ID"]) == entrada or cliente["Nome"].lower() == entrada.lower():
            print(f'Nome: {cliente["Nome"]}')
            print(f'E-mail: {cliente["E-mail"]}')
            print(f'Telefone: {cliente["Telefone"]}')
            return
        
    print("Cliente não encontrado.")
    valores_aproximados_clientes(entrada)




def pesquisar_produtos():
    with open("produtos.json", "r") as arquivo:
        produtos = json.load(arquivo)

    entrada = input("Informe o ID ou o nome do produto: ")

    for produto in produtos:
        if str(produto["ID"]) == entrada or produto["Nome"].lower() == entrada.lower():
            print(f'Nome: {produto["Nome"]}')
            print(f'Descrição: {produto["Descrição"]}')
            print(f'Preço: {produto["Preço"]}')
            return
        
    print("Produto não encontrado.")
    valores_aproximados_produtos(entrada)


def pesquisar_compra():
    with open("compras.json", "r") as arquivo:
        compras = json.load(arquivo)

    entrada = input("Informe o ID da compra: ")

    for compra in compras:
        if str(compra["ID"]) == entrada or str(compra["ID Cliente"]) == entrada or compra["Data"] == entrada or compra["Nome do cliente"].lower() == entrada.lower():
            print(f'Data: {compra["Data"]}')
            print(f'E-mail: {compra["ID Cliente"]}')
            print(f'Valor total: {compra["Valor Total"]}')
            print(f'Forma de pagamento: {compra["Forma de pagamento"]}')
            print(f'Produtos: {compra["Produtos comprados"]}')
            return

    print("Compra não encontrada.")


def valores_aproximados_clientes(x):
    with open("clientes.json","r") as arquivo:
        clientes = json.load(arquivo)
    clientes_aproximados = []

    for cliente in clientes:
        if cliente['Nome'][0].lower() == x[0].lower():
            clientes_aproximados.append(cliente)

    if len(clientes_aproximados) == 0:
        print("Nenhum cliente encontrado.")

    elif len(clientes_aproximados) == 1:
        print("Cliente encontrado:")
        print((clientes_aproximados[0]))

    else:
        print("Tente por:")
        for cliente in clientes_aproximados:
            print(f'Cliente: {cliente["Nome"]}')

def valores_aproximados_produtos(x):
    with open("produtos.json","r") as arquivo:
        produtos = json.load(arquivo)
    produtos_aproximados = []

    for produto in produtos:
        if produto['Nome'][0].lower() == x[0].lower():
            produtos_aproximados.append(produto)

    if len(produtos_aproximados) == 0:
        print("Nenhum produto encontrado.")

    elif len(produtos_aproximados) == 1:
        print("Produto encontrado:")
        print((produtos_aproximados[0]))

    else:
        print("produtos aproximados encontrados:")
        for produto in produtos_aproximados:
            print((produto))

def listar_comprasdata():
    with open('compras.json') as arquivo:
        informacoes= json.load(arquivo)
    while True:
        data = input('Informe a data na qual deseja listar as compras (dia/mês/ano):\n')
        verificar_data(data)
        if verificar_data(data):
            break
        else:
            print("Data inválida!")
            continue
    print('\nInformações das compras na data ',data,'são: \n----------------------------------\n')
    for x in informacoes:
        if x["Data"] == data:
            print (f'ID: {x["ID"]}\nID Cliente: {x["ID Cliente" ]}\nNome do cliente:{x["Nome do cliente"]}\nForma de pagamento: {x["Forma de pagamento"]}\nData: {x["Data"]}\nValor Total: {x["Valor Total"]}\nProdutos comprados: {x["Produtos comprados"]}')
    return


def listar_compraspag():
    with open('compras.json') as arquivo:
        informacoes= json.load(arquivo)
    while True:
        forma = input('Informe a forma de pagamento na qual deseja listar as compras: ').title()
        if forma not in ["Pix", "Dinheiro", "Cartão"]:
            print("Forma de pagamento inválida! Verifique se digitou corretamente.")
            continue
        break
    print('\nInformações das compras na forma de pagamento ',forma,'são: \n----------------------------------\n')
    for x in informacoes:
        if x["Forma de pagamento"] == forma:
            print (f'ID: {x["ID"]}\nID Cliente: {x["ID Cliente" ]}\nNome do cliente:{x["Nome do cliente"]}\nForma de pagamento: {x["Forma de pagamento"]}\nData: {x["Data"]}\nValor Total: {x["Valor Total"]}\nProdutos comprados: {x["Produtos comprados"]}')
    return


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

