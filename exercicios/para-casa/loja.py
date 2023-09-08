# Quero opção de:

# Adicionar doce

# Exibir detalhe de um doce

# Atualizar doce

# Apagar doces

# Exibir a lista de todos os doces

 

import time

 

# Removi e alterei a lista de produtos, pois quando rodava o codigo as

# informações que apareciam estavam embaralhadas e sem sentido a respeito do pedido da usuaria #

lista_produtos = [{'id': 1, 'nome': 'Bombom', 'preço': 1.50},

                  {'id': 2, 'nome': 'Trufado', 'preço': 3.0},

                  {'id': 3, 'nome': 'Pudim', 'preço': 8.0},

                  {'id': 4, 'nome': 'Bolo', 'preço': 26.0}]

 

id_produto = 1

def menu():

    while True:

        print("\n ** MENU LOJA REPROGRAMA **\n")

        print("1 - Adicionar")

        print("2 - Exibir detalhes")

        print("3 - Atualizar")

        print("4 - Apagar")

        print("5 - Exibir todos")

        print("0 - Sair")

 

        opcao = input("Escolha a opção desejada\n")

 

        if opcao == "1":

            adicionar_produto()

        elif opcao == "2":

            print("opcao exibir detalhes doce")

        elif opcao == "3":

            atualizar_produto()

        elif opcao == "4":

            print("opcao apagar doce")

        elif opcao == "5":

            listar_todos()

        elif opcao == "0":

            break

        else:

            print("Opção inválida, por favor escolha uma opção do menu")

 

 # Não alterei nada do codigo #

def gerar_id_produto():

    if len(lista_produtos) == 0:

        return 1

    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)

    novo_id = lista_produtos[0].get("id") + 1

 

    return novo_id

def adicionar_produto():

    nome_produto = input("Digite o nome do produto:\n")

    preco_produto = input("Digite o preço do produto:\n")

 

    produto = {

        "id": gerar_id_produto(),

        "nome": nome_produto,

        "preço": float(preco_produto),

    }

    lista_produtos.append(produto)

 

    print(lista_produtos)

 

 # Não alterei nada do codigo #

 

# Criei uma lista suspensa de exibição de doçes #

def exibir_detalhes_doce(lista_produtos):

    print('Detalhes do doce:')

    print(f'id :{lista_produtos["id"]}')

    print(f'nome: {lista_produtos["nome"]}')

    print(f'preço: R${lista_produtos["preço"]: .2f}')

   

 

def atualizar_produto():

    id_produto = input("Digite o ID do produto para atualizar:\n")

 

    for index in range(len(lista_produtos)):

        if lista_produtos[index].get("id") == int(id_produto):

            novo_valor = input("Digite o novo valor do produto:\n")

            lista_produtos[index]["preço"] = float(novo_valor)

            print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")

 

def listar_todos():

    for index in range(len(lista_produtos)):

        print(f"{lista_produtos[index]}\n")

 

 

menu()