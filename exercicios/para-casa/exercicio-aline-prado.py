# Quero opção de:
# Adicionar doce
# Exibir detalhe de um doce
# Atualizar doce
# Apagar doces
# Exibir a lista de todos os doces
import time

lista_produtos = [{'id': 3, 'nome': 'asdasdas', 'preço': 32.0}, {'id': 2, 'nome': 'asd', 'preço': 2.0}, {'id': 1, 'nome': 'a', 'preço': 1.0}, {'id': 4, 'nome': '23123', 'preço': 13123.0}]

id_produto = 1
def menu():
    # PONTO DE MELHORIA: Adicionei um subtítulo ao programa usando print para ficar claro ao usuário 
    # que a finalidade do programa é a gestão dos produtos que seram inseridos na loja.
    while True:
        print("\n ** MENU LOJA REPROGRAMA **\n")
        print("\n ** GESTÃO DOS PRODUTOS **\n") 
        print("1 - Adicionar ") 
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")

        opcao = input("Escolha a opção desejada\n")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            exibir_detalhes_produto()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            apagar_produto()
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

    # PONTO DE MELHORIA: Adicionei o bloco try-except para evitar quebrar o programa caso uma string seja digitada nos inputs de preço. 
    # O script tenta converter a variável preco_produto em um número float usando float(preco_produto). 
    # Se isso não ocorre, ou seja o usuário digitar um valor diferente do esperado, o programa exibe uma mensagem amigável sobre o erro.

    try:
        preco_produto = float(preco_produto)
    except ValueError:
        print("Valor inválido para o preço. Certifique-se de digitar um número válido.")
        return

    produto = {
        "id": gerar_id_produto(),
        "nome": nome_produto,
        "preço": float(preco_produto),
    }
    lista_produtos.append(produto)

    print(lista_produtos)



def atualizar_produto():
    id_produto = input("Digite o ID do produto para atualizar:\n")

  # Repliquei a estratégia do try-except em atualizar produto para garantir que o id é um int, e o preço um float.
    try: 
    
        for index in range(len(lista_produtos)):
            if lista_produtos[index].get("id") == int(id_produto):
                novo_valor = input("Digite o novo valor do produto:\n")
                lista_produtos[index]["preço"] = float(novo_valor)
                print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")
                novo_valor = float(novo_valor)
                id_produto = int(id_produto)
    except ValueError:
            print("Valor inválido para o preço. Certifique-se de digitar um número válido.")
            return


def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")


def exibir_detalhes_produto():
    id_produto = input("Digite o ID do produto para exibir os detalhes:\n")
    encontrado = False

    for produto in lista_produtos:
        if produto["id"] == int(id_produto):
            print("Detalhes do Produto:")
            print(f"ID: {produto['id']}")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: {produto['preço']}")
            encontrado = True
            break

    if not encontrado:
        print("Produto não encontrado.")

def apagar_produto():
    id_produto = input("Digite o ID do produto para apagar:\n")
    encontrado = False

    for produto in lista_produtos:
        if produto["id"] == int(id_produto):
            lista_produtos.remove(produto)
            print("Produto apagado com sucesso.")
            encontrado = True
            break

    if not encontrado:
        print("Produto não encontrado.")


menu()
