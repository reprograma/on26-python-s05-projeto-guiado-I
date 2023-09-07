#CRUD = CRIAR, LER, ATUALIZAR E DELETAR
#Menu
#Opções: 
#Adicionar doces
#Listar doces detalhada
#Atualizar produto
#Apagar produto
#Exibir a lista de todos os doces
#**Criar opção de voltar**
lista_produtos = [
    {"id": 2, "nome": "novo produto2 ", "preço": 3.0},
    {"id": 3, "nome": "novo produto3 ", "preço": 4.0},
    {"id": 1, "nome": "novo produto1 ", "preço": 3.0},    
]


def menu():
    while True:
        print("\n ** MENU STORE MAY **\n")
        print("1 - Adicionar ")
        print("2 - Exibir detalhes ")
        print("3 - Atualizar ")
        print("4 - Apagar ")
        print("5 - Exibir todos ")
        print("0 - Sair do menu ")
        
        opcao = input("Escolha a opção desejada\n")
        
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            print("Exibir detalhes ")
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            print("Apagar doces ")
        elif opcao == "5":
            listar_todos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Por favor escolher uma opção do menu.")
    
    
def adicionar_produto():
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = float(input("Digite o preço do produto:\n"))
    
    produto = {"id": gerar_id_produto(), "Nome": nome_produto, "Preço": float(preco_produto)}
    
    lista_produtos.append(produto)
    
    print(lista_produtos)

def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=id, reverse=True)

    novo_id = lista_produtos[0].get("id") + 1

    return novo_id
    
def atualizar_produto():
    id_produto = input("Digite o ID do produto para atualizar:\n")
    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("id") == int(id_produto):
            novo_valor = input("Digite o novo valor do produto:\n")
            lista_produtos[index]["preço"] == float(novo_valor)
        print(f"Produto atualizado com sucesso! {lista_produtos[index]}")
    

def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")    

menu()
