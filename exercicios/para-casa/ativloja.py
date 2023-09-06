"""
Todas as funções e variáveis tiveram seus nomes colocados em inglês para ficar melhor caracterizado e de melhor entendimento de que se trata de um CRUD. 
Faz parte de uma boa prática ter as variáveis em inglês.
"""


product_list = []

def menu():

    while True:
        print('\n * MENU LOJA REPROGRAMA *\n')
        print('1 - Adicionar')
        print('2 - Exibir detalhes')
        print('3 - Atualizar')
        print('4 - Apagar')
        print('5 - Exibir todos')
        print('0 - Sair')

        opcao = input('Escolha a opção desejada:\n')

        if opcao == '1':
            create_product()
        elif opcao == '2':
            read_product()
        elif opcao == '3':
            update_product()
        elif opcao == '4':
            delete_product()
        elif opcao == '5':
            list_all()
        elif opcao == '0':
            break
        else:
            print('Opção inválida, por favor escolha uma opção do menu')

"""
Adiciona um novo produto à lista. Ela solicita o nome e o preço do produto au usuário, cria um dicionário com essas informações, gera um ID
para o produto e adiciona ele à lista. Criei um FOR para que antes de adicionar um novo produto, ela verifica se um produto com o mesmo nome já existe.
"""
def create_product():
    name_product = input("Digite o nome do produto:\n")
    price_product = input("Digite o preço do produto:\n")

    product = {
        "id": generate_id(),
        "nome": name_product,
        "preço": float(price_product)
    }

    for existent_product in product_list:
        if existent_product["nome"] == name_product:
            print("O produto já existe!")
            return

    product_list.append(product)

"""
Permite ao usuário visualizar os detalhes de um produto com base em seu ID. Ela solicita o ID do produto, 
verifica se o número do ID é válido, pesquisa na lista de produtos e exibe os detalhes do produto correspondente.
"""
def read_product():
    id_product = input("Informe o ID do produto para listar:\n")
    while True:
        try:
            float(id_product)
            break
        except ValueError:
            print("O ID informado não é válido.")
            id_product = input("Informe o ID do produto para listar:\n")

    try:
        for index in range(len(product_list)):
            if product_list[index].get("id") == int(id_product):
                print("Segue o produto selecionado: ", product_list[index])
                break
        else:
            print("ID não localizado. Tente novamente.")
    except ValueError:
        print("ID não localizado. Tente novamente.")

"""
Gera um ID para o produto adicionado. Se a lista de produtos estiver vazia, o ID é definido como 1. 
Caso contrário, ele verifica o maior ID existente na lista de produtos e adiciona 1 a esse valor para criar um novo ID exclusivo e isso é feito por conta da função LAMBDA.
"""
def generate_id():
    if not product_list:
        return 1

    product_list.sort(key=lambda product: product.get("id"), reverse=True)

    new_id = product_list[0].get('id') + 1
    return new_id

"""
 Atualiza o preço de um produto existente com base no seu ID. O usuário fornece o ID do produto que deseja atualizar e, em 
 seguida, insere o novo preço para o produto. A função pesquisa o produto na lista pelo ID e atualiza o preço.
 """
def update_product():
    id_product = input("Digite o ID do produto para atualizar:\n")

    for index in range(len(product_list)):
        if product_list[index].get("id") == int(id_product):
            new_value = input("Digite o novo valor do produto:\n")
            product_list[index]["preço"] = float(new_value)
            print(f"O produto foi atualizado com sucesso! {product_list[index]}")

"""
Exibe todos os produtos na lista de produtos. Ela itera(passa) por todos os produtos e os imprime na tela.
"""
def list_all():
    for index in range(len(product_list)):
        print(f"{product_list[index]}\n")

"""
Permite ao usuário excluir um produto com base em seu ID. O usuário fornece o ID do produto que deseja excluir, e a função 
pesquisa o produto na lista e o remove se for encontrado.
"""
def delete_product():
    id_product = int(input('Insira o ID do produto:\n'))

    for product in product_list:
        if product["id"] == id_product:
            product_list.remove(product)
            print(f'Produto deletado: {product}')
            break
    else:
        print("ID não encontrado na lista de produtos.")

menu()