# CRUD = CREATE, READE, UPDATE, DELETE
# LOJA DE DOCES

import time

lista_produtos = [
    {"COD": 3, "nome": "BIGBIG", "preco": 1.0},
    {"COD": 2, "nome": "Chokito", "preco": 1.0}, 
    {"COD": 1, "nome": "Mentos", "preco": 4.0}, 
    {"COD": 4, "nome": "Sonho de Valsa", "preco": 52.0}
    ]

cod_produto = 1

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
            exibir_detalhes()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            deletar()
        elif opcao == "5":
            listar_todos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida, por favor escolha uma opção do menu")


def gerar_cod_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=lambda produto: produto.get("COD"), reverse=True)
    novo_cod = lista_produtos[0].get("COD") + 1

    return novo_cod


def adicionar_produto():
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = input("Digite o preço do produto:\n")

    produto = {
        "COD": gerar_cod_produto(),
        "nome": nome_produto,
        "preço": float(preco_produto),
    }
    lista_produtos.append(produto)

    print(lista_produtos)


def atualizar_produto():
    cod_produto = input("Digite o código do produto para atualizar:\n")

    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("COD") == int(cod_produto):
            novo_valor = input("Digite o novo valor do produto:\n")
            lista_produtos[index]["preço"] = float(novo_valor)
            print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")


def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")


def exibir_detalhes():
    cod_doce = input("Forneça o código do produto: ")
    for produto in lista_produtos:
        if produto.get("COD") == int(cod_doce):
            print(produto)
            break
        

def deletar():
    cod_produto =input("Digite o código do produto para deletar: ")
    for produto in lista_produtos:
        if produto.get("COD") == int(cod_produto):
            lista_produtos.remove(produto)
            break      #para não ter que passar por todos os itens


menu()
