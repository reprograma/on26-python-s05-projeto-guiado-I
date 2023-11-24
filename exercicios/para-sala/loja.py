
# Quero opção de:
# Adicionar doce
# Exibir detalhe de um doce
# Atualizar doce
# Apagar doces
# Exibir lista de doces

lista_produtos = []


def menu():
    while True:
        print("\n ** MENU LOJA REPROGRAMA **")
        print("1 - Adicionar")
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")

        opcao = input("Escolha a opção desejada \n")

        if opcao == "1":
            adicionar_produto()
        elif  opcao == "2":
            print ("Opção exibir detalhes")        
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            print ("Opção apagar")
        elif opcao == "5":
            print ("Opção exibir todos")
        elif opcao == "0":
            print ("Opção sair")
            break
        else:
            print ("Opção inválida. Por favor, escolha uma opção do menu.")
    
def adicionar_produto():
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = input("Digite o preço do produto:\n")

    produto = {"id":gerar_id_produto(),"nome":nome_produto,"preço": float(preco_produto)}

    lista_produtos.append(produto)
    print(lista_produtos)

def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=id, reverse=True)
    novo_id = lista_produtos[0].get("id")+1
    return novo_id

def atualizar_produto():
    id_produto = input("Digite o ID do produto para atualizar:\n")
    
    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("") == int(id_produto):
            print("Produto encontrado")

def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")
        
menu()