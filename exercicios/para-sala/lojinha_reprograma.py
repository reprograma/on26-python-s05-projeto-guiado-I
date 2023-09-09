# quero opção de:
# Adicionar novo doce
# Exibir detalhes de um doces
# Atualizar doces
# Apagar doces
# Exibir a lista de todos os doces

lista_produtos = []

def menu():
    while True:
        print("\n ** MENU LOJA REPROGRAMA **\n")
        print("1 - Adicionar")
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")
        
        opcao = input("Escolha a opção desejada:\n")
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            exibir_detalhes()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            exibir_produtos()
        elif opcao == "0":
            print("Sair")
            break
        else:
            print("Opção inválida, por favor escolha uma opção do menu.")


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


def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_produtos[0].get("id") + 1
    return novo_id

def exibir_detalhes():
    id_produto = int(input("Digite o ID do produto para exibir detalhes: "))
    for produto in lista_produtos:
        if produto["id"] == id_produto:
            print(f"Os detalhes do produto {id_produto}: {produto['detalhes']}")
            return
    print(f"Produto com ID {id_produto} não foi encontrado.")

def atualizar_produto():
    id_produto = input("Digite o ID do produto para atualizar:\n")

    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("") == int(id_produto):
            novo_valor = input("Digite o novo valor do produto:\n")
            lista_produtos[index]["preço"] = novo_valor
            print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")

def remover_produtos():
    id_produto = int(input("Digite o ID do produto que deseja remover: "))
    for produto in lista_produtos:
        if produto["id"] == id_produto:
            lista_produtos.remove(produto)
            print(f"Produto com ID {id_produto} foi removido do catálogo.")
            return
    print(f"Produto com ID {id_produto} não foi encontrado.")


def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")


menu()