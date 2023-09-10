# Quero opção de:
# Adicionar doce
# Exibir detalhe de um doce
# Atualizar doce
# Apagar doces
# Exibir a lista de todos os doces

# Apaguei o import time devido a professora ter esquecido no código.

#Alterei os valores, nomes e preço da lista.
lista_produtos = [{'id': 1, 'nome': 'jujuba', 'preço': 2.0}, {'id': 2, 'nome': 'caramelo', 'preço': 3.0}, {'id': 3, 'nome': 'fini', 'preço': 5.0}, {'id': 4, 'nome': 'pão de mel', 'preço': 10.0}]

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
            exibir_detalhes()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            deletar_item()
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
def adicionar_produto():
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = input("Digite o preço do produto:\n")

    produto = {"id": gerar_id_produto(),"nome": nome_produto,"preço": float(preco_produto)}
    lista_produtos.append(produto)

    print(lista_produtos)


def exibir_detalhes():
    mostrar_detalhes = int(input("Digite o id do item para exibir detalhes: "))
    for produto in lista_produtos:
        if produto.get("id") == lista_produtos("id"):
            print(f"Aqui está os detalhes do item que você selecionou mostrar_detalhes")
        else: 
            print("ID inexistente")
        break


def atualizar_produto():
    id_produto = input("Digite o ID do produto para atualizar:\n")

    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("id") == int(id_produto):
            novo_valor = input("Digite o novo valor do produto:\n")
            lista_produtos[index]["preço"] = float(novo_valor)
            print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")


def deletar_item():
    id_produto = int(input("Digite o ID do item para deletá-lo: "))
    for produto in lista_produtos:
        if produto.get("id") == int(id_produto):
            list.remove(produto)
            print("Item excluído!")


def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")

  

menu()
