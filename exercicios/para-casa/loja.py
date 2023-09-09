lista_produtos = [
    {"id": 3, "nome": "asdasdas", "preço": 32.0},
    {"id": 2, "nome": "asd", "preço": 2.0},
    {"id": 1, "nome": "a", "preço": 1.0},
    {"id": 4, "nome": "23123", "preço": 13123.0},
]

id_produto = 1


def menu():
    """
    Essa função executa o menu no programa

    Args:
       **None**

    Returns:
        str: value

    Exemplo de uso:
        >>> menu(1)
         ** MENU LOJA REPROGRAMA **

            1 - Adicionar\n
            2 - Exibir detalhes\n
            3 - Atualizar\n
            4 - Apagar\n
            5 - Exibir todos\n
            0 - Sair\n
    """
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


def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_produtos[0].get("id") + 1

    return novo_id


def adicionar_produto(abc):
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


def listar_todos():
    for produto in lista_produtos:
        print(f"{produto}\n")


def exibir_detalhes():
    id_doce = input("forneça o ID do produto:\n")
    for produto in lista_produtos:
        if produto.get("id") == int(id_doce):
            print(produto)
            break


def deletar():
    id_produto = input("Digite o ID do produto para deletar:\n")

    for produto in lista_produtos:
        if produto.get("id") == int(id_produto):
            lista_produtos.remove(produto)
            break


menu()
