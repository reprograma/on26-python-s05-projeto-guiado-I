 
import time

lista_de_produtos = []  #lista onde serão armazenados os dados dos produtos

def menu():
    while True:
        print("\n MENU LOJA REPROGRAMA\n")
        print("1 - Adicionar")
        print("2 - Exibir detalhes do produto")
        print("3 - Atualizar dados do produto")
        print("4 - Excluir")
        print("5 - Exibir todos os produtos")
        print("0 - Sair")

        opcao = input("Escolha a opção desejada:\n")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            exibir_um_produto()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            excluir_um_produto()
        elif opcao == "5":
            listar_todos_os_produtos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opçãp do menu.")

#Função gerador_de_id: gera automaticamente uma id exclusiva para cada produto
def gerador_de_id():
    if len(lista_de_produtos) == 0:                                            #atribui ID 1 para o primeiro produto incluídos na lista
        return 1
    lista_de_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_de_produtos[0].get("id") + 1                        #pega o valor do id do primeiro item da lista de produtos e adiciona mais 1. obs: o get extrai o valor de uma das chaves do dicionário

    return novo_id

#Função adicionar_produto: lê os dados do produto informados pelo usuário e adiciona essas informações, por meio da variável "produto", na lista "lista_de produtos"
def adicionar_produto():
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = float(input("Digite o preço do produto:\n"))

    produto = {
        "id": gerador_de_id(), 
        "nome": nome_produto, 
        "preço": preco_produto
    }

    lista_de_produtos.append(produto)

    print(lista_de_produtos)

#Função atualizar_produto: permite ao usuário alterar o preço de um produto
def atualizar_produto():
    id_produto = input("Qual é a ID do produto que deseja atualizar? ")
    for index in range(len(lista_de_produtos)):
        if lista_de_produtos[index].get("id") == int(id_produto):
            nome_do_doce = lista_de_produtos[index].get("nome")                                    # Fiz uma pequena mudança acrescentando essa variável para ficar mais evidente para o usuário qual é o produto com o qual ele está lidando.
            novo_preco_do_produto = (input(f"Qual será o novo preço do produto {nome_do_doce}? "))   # Mudei o nome da variável só por uma questão de consistência: sempre usarmos a palavra "preço" para nos referirmos ao valor do produto.
            lista_de_produtos[index]["preço"] = float(novo_preco_do_produto)
            print(f"O preço de {nome_do_doce} foi atualizado.")
        

def listar_todos_os_produtos():
    for index in range(len(lista_de_produtos)):
        print(f"{lista_de_produtos[index]}\n")

def excluir_um_produto():
    id_do_produto = (input("Qual é o ID do produto que você pretende excluir? "))
    for doce in range(len(lista_de_produtos)):
        if lista_de_produtos[doce].get("id") == int(id_do_produto):
            
            print(f'O produto {lista_de_produtos[doce].get("nome")} foi excluído.')
        
            lista_de_produtos.remove(lista_de_produtos[doce])
    
# Pensei e pensei em como elaborar uma "trava" para caso o usuário digite um ID que não existe na lista, mas ela não funcionou para o produto 
# de ID 1 (curiosamente funcionou para outros, como o de ID 4, por exemplo). Resolvi deixar em comentário (para mostrar que tentei): 
#def exibir_um_produto():
    #id_prod = (input("Qual é a id do produto que você deseja consultar? "))
    #for prod in range(len(lista_de_produtos)):
        #list_ids = []
        #list_ids.append(lista_de_produtos[prod].get("id"))
    #if int(id_prod) in list_ids: 
        #if lista_de_produtos[prod].get("id") == int(id_prod):
            #print(lista_de_produtos[prod])
    #else:
        #print("Não encontramos um produto com esse ID. Por favor, digite um valor de ID válido.") 

def exibir_um_produto():
    id_prod = (input("Qual é o ID do produto que você deseja consultar? "))
    for prod in range(len(lista_de_produtos)):
        if lista_de_produtos[prod].get("id") == int(id_prod):
            
            print(lista_de_produtos[prod])

menu()

