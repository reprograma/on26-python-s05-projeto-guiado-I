# começamos com uma lista vazia de produtos
lista_produtos = []

# variável id_produto passa a existir
id_produto = 1

# função menu() abre o menu com que vamos trabalhar
def menu():

    # while garante um loop, ou seja, o usuário sempre retorna ao menu
    while True:

        # prints permitem que usuário visualize opções
        print("\n ** MENU LOJA REPROGRAMA ** \n" )
        print("1 - Adicionar")
        print("2 - Exibir detalhes" )
        print("3 - Atualizar" )
        print("4 - Apagar" )
        print("5 - Exibir todos" )
        print("0 - Sair" )

        opcao = input("Escolha a opção desejada\n")

        # condicionais estabelecem as principais funções do programa
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            exibir_detalhes()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            deletar_produto()
        elif opcao == "5":
            listar_todos()
        elif opcao == "0":
            break
        else: print("Opção inválida, por favor escolha uma opção válida")

# a função gerar_id_produto() funciona da seguinte maneira: ao começo do programa, se a lista está zerada,
# a função retorna o valor 1 para o primeiro ID.
# conforme são gerados novos produtos, a função ordena os itens de maneira decrescente ("reverse=True")
# para que o último item da lista esteja no primeiro parâmetro da função [0]
# desta forma, o ID de número mais alto é facilmente encontrado, 
# e a ele é possível adicionar 1 para gerar o novo ID

def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_produtos[0].get("id") + 1
    
    return novo_id

def adicionar_produto():
    
    nome_produto = input("Digite o nome do produto\n")
    preco_produto = input("Digite o preço do produto\n")

    # à função original foi acrescido um laço while para garantir que o preço inserido seja um numeral
    # se não for possível executar a função float() - ou seja, se o input for str -
    # o programa reconhece o erro e recomeça o input 

    while True:
        try:
            float(preco_produto)
            break
        except ValueError:
            print("O preço informado precisa ser um número. Insira um valor válido.")
            preco_produto = input("Digite o preço do produto\n")
    
    # novo produto é gerado com as respectivas chaves
    produto = {
        "id": gerar_id_produto(), 
        "nome":nome_produto, 
        "preço":float(preco_produto)
        }

    # novo produto é acrescido à lista usando a função append
    lista_produtos.append(produto)

    print("A lista foi atualizada com sucesso!\n", lista_produtos)

def exibir_detalhes():
    id_produto = input("Informe o ID do produto para exibir detalhes:\n") 
    
    # mesma garantia de que o usuário informe um número para o ID
    try:
        float(id_produto)
    except ValueError:
            print("O ID informado precisa ser um número. Insira um valor válido.")
            id_produto = input("Informe o ID do produto para exibir detalhes:\n") 
    
    # localizando o produto por seu ID - tratativas de erro caso o ID informado não esteja na lista
    try:
        id_produto = int(id_produto)
        for produto in lista_produtos:
            if produto.get("id") == id_produto:
                print("Detalhes do produto:", produto)
                break
            if produto.get("id") not in range(len(lista_produtos)):
                print("Não foi possível localizar o ID. Tente novamente e informe um ID válido")
                break
    except ValueError:
        print("Não foi possível localizar o ID. Tente novamente e informe um ID válido")     

def atualizar_produto():
    id_produto = input("Informe o ID do produto para atualizar:\n")

    # função localiza o produto pelo ID e permite que usuário insira novos nome e valor
    try:
        id_produto = int(id_produto)
        for produto in lista_produtos:
            if produto.get("id") == id_produto:
                novo_nome = input("Digite o novo nome do produto: ")
                novo_valor = input("Digite o novo valor do produto: ")
                # atualiza os itens do dicionário sobrescrevendo o valor das chaves "nome" e "preço"
                try:
                    novo_valor = float(novo_valor)
                    produto["nome"] = novo_nome
                    produto["preço"] = novo_valor
                    print("O produto foi atualizado com sucesso!")
                    print(produto)
                    break
                except ValueError:
                    print("Preço inválido. Certifique-se de inserir um número válido para o preço.")
                break
        else:
            print("Não foi possível localizar o ID. Tente novamente e informe um ID válido.")
    except ValueError:
        print("O ID informado precisa ser um número inteiro. Insira um valor válido.")

def deletar_produto():
    id_produto = input("Informe o ID do produto para remover:\n")

    while True:
        try:
            float(id_produto)
            break
        except ValueError:
            print("O ID informado precisa ser um número. Insira um valor válido.")
            id_produto = input("Informe o ID do produto para exibir detalhes:\n")

    # localizando o produto e removendo-o com a função pop
    
    try:
        for index in range(len(lista_produtos)):
            if lista_produtos[index].get("id") == int(id_produto):
                lista_produtos.pop(index)
                print("Produto removido. A lista foi atualizada com sucesso")
                print(lista_produtos)
            elif lista_produtos[index].get("id") not in range(len(lista_produtos)):
                print("Não foi possível localizar o ID. Tente novamente e informe um ID válido")
                break    
    except ValueError:
        print("Não foi possível localizar o ID. Tente novamente e informe um ID válido") 

# imprime uma lista dos produtos
def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")

menu()
