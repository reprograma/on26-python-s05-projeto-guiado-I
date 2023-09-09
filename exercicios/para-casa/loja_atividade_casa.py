# Quero opção de:
# Adicionar doce
# Exibir detalhe de um doce
# Atualizar doce
# Apagar doces
# Exibir a lista de todos os doces

# Foram utilizadas docstrings conforme boas práticas de documentação

# Primeiro de tudo foi retirada a biblitotca "time" que não é necessária

# Dois problemas no id 4: preço estranho, diria para o usuário verificar erro de digitação,
# inclusive no nome do produto que ao invés de letras possui números
# (como estava: {'id': 4, 'nome': '23123', 'preço': 13123.0}])
# Alterei os nomes dos produtos para melhor entendimento deste exemplo/projeto
# Apesar do sort fazer com que a lista seja ordenada durante a execução, é uma boa prática manter 
# a lista em uma ordem consistente para facilitar a leitura e a manutenção do código.
lista_produtos = [{'id': 1, 'nome': 'Paçoca', 'preço': 2.0},
                  {'id': 2, 'nome': 'Goiabada', 'preço': 5.0},
                  {'id': 3, 'nome': 'Brigadeiro', 'preço': 4.0},
                  {'id': 4, 'nome': 'Bananinha', 'preço': 3.0}]

# Retirei a função "id_produto = 1" que não estava sendo usada

def menu():
    """
    Exibe um menu para o usuário e permite que ele escolha entre várias opções.

    1 - Adicionar: Permite ao usuário adicionar um novo produto à lista.
    2 - Exibir detalhes: Exibe os detalhes de um produto específico com base em seu ID.
    3 - Atualizar: Permite ao usuário atualizar o preço de um produto com base em seu ID.
    4 - Apagar: Permite ao usuário apagar um produto da lista com base em seu ID.
    5 - Exibir todos: Exibe a lista de todos os produtos.
    0 - Sair: Encerra o programa.
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
            exibir_detalhes_produto()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            apagar_produto()
        elif opcao == "5":
            listar_todos()
        elif opcao == "0":
            break
        # Alterei a frase retirando o "opção inválida"
        # para fazer sentido também no início do menu, em que ainda não foi digitado nada
        else:
            print("Por favor escolha uma opção do menu")

def gerar_id_produto():
    """
    Gera um novo ID para um produto com base no ID máximo atual na lista de produtos.

    """
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_produtos[0].get("id") + 1

    return novo_id

def adicionar_produto():
    """
    Permite ao usuário adicionar um novo produto à lista de produtos.

    Solicita o nome e o preço do produto e adiciona o produto à lista.
    """
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = input("Digite o preço do produto:\n")

    produto = {
        "id": gerar_id_produto(),
        "nome": nome_produto,
        "preço": float(preco_produto),
    }
    lista_produtos.append(produto)
    
    # Um feedback ao usuário foi acrescentado
    print("Produto adicionado")
    print(lista_produtos)
    
# Funçao adicionada
def exibir_detalhes_produto():
    """
    Exibe os detalhes de um produto com base em seu ID.

    Solicita ao usuário o ID do produto e mostra seus detalhes, incluindo nome e preço.
    """
    id_produto = input("Digite o ID de um produto para visualizar seus detalhes:\n")
    produto_encontrado = None

    for produto in lista_produtos:
        if produto.get("id") == int(id_produto):
            produto_encontrado = produto
            break

    if produto_encontrado:
        print("Detalhes do produto:")
        print(f"ID: {produto_encontrado['id']}")
        print(f"Nome: {produto_encontrado['nome']}")
        print(f"Preço: R${produto_encontrado['preço']:.2f}")
    else:
        print("ID inválido")
        
# Função adicionada
def apagar_produto():
    """
    Permite ao usuário apagar um produto da lista com base em seu ID.

    Solicita ao usuário o ID do produto a ser apagado e remove-o da lista.
    """
    id_produto = input("Para apagar um produto do sistema, digite seu ID:\n")
    produto_encontrado = None

    for produto in lista_produtos:
        if produto.get("id") == int(id_produto):
            produto_encontrado = produto
            break
    # Melhoria para feedback ao cliente 
    if produto_encontrado:
        lista_produtos.remove(produto_encontrado)
        print("O produto foi apagado.")
    else:
        print("Produto não encontrado.")

def atualizar_produto():
    """
    Permite ao usuário atualizar o preço de um produto com base em seu ID.

    Solicita ao usuário o ID do produto e o novo preço, atualizando-o na lista.
    """
    id_produto = input("Digite o ID do produto para atualizar:\n")

    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("id") == int(id_produto):
            novo_valor = input("Digite o novo valor do produto:\n")
            lista_produtos[index]["preço"] = float(novo_valor)
            print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")

def listar_todos():
    """
    Exibe a lista de todos os produtos.

    Itera pela lista de produtos e imprime os detalhes de cada produto.
    """
    for produto in lista_produtos:
        print(f"ID: {produto['id']}")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R${produto['preço']:.2f}\n")

# Chamada para a função menu para iniciar o programa
menu()


