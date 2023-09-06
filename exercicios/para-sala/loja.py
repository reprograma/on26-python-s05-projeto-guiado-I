#Quero opção de:
#CRUD
#Adicionar doce
#Ler doce
#Atualizar doce
#Apagar doce
#Exibir a lista de todos os doces

import time

lista_produtos = [{'id': 3, 'nome': 'chocolate', 'preço': 8.0}, {'id': 2, 'nome': 'chocolate', 'preço': 8.0}, {'id': 1, 'nome': 'amora', 'preço': 5.0}, {'id': 4, 'nome': 'pudim', 'preço': 9.0}]

id_produto_del = ()

id_produto = 1

def menu():
    while True:
        print("/n ** MENU LOJA REPROGRAMA **")
        print("1 - Adicionar")
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")

        opcao = input("Escolha a opção desejada\n")

        print(opcao)

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            print("opcao exibir detalhes do doce") #fazer
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            deletar_produto()
        elif opcao == "5":
            listar_todos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida, por favor escolha uma opção do menu. :)")

    
     #As ações do programa       

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

def atualizar_produto():
    id_produto = input("Digite o ID do produto para atualizar:\n")

    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("id") == int(id_produto):
            novo_valor = input("Digite o novo valor do produto:\n")
            lista_produtos[index]["preço"] = float(novo_valor)
            print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")


def deletar_produto():
    id_produto = input("Digite o ID do produto para deletar:\n")

    lista_produtos.remove(id_produto)
    print(f"O produto foi removido com sucesso:\n")


def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")


menu()
