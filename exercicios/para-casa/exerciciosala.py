#CRUD = create, reade, update, delete

#criar doce
#exibir detalhe de um doce
#atualizar doce
#apagar doce
#exibir a lista de todos os doces

lista_produtos = [
    {"id": 2, "nome": "novo produto2", "preço": 3.0},
    {"id": 3, "nome": "novo produto3", "preço": 4.0},
    {"id": 1, "nome": "novo produto1", "preço": 3.0},
]

def menu():
    while True:
        print("\n ** MENU LOJA REPROGROMA ** \n")
        print("1 - Adicionar")
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")

        opcao = input("Escolha de opção desejada: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            print("\n opção exibir detalhes doce\n")
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            print("\n opção apagar doce\n")
        elif opcao == "5":
            listar_todos()
        elif opcao == "0":   
            print("\n ** sair **\n")
            break
        else:
            print("\n ** opcao invalida **\n")
    
        
def adicionar_produto():
    nome_produto = input("digite o nome do produto: \n")
    preco_produto = input("digite o preço do produto: \n")
    
    produto = {
        "id": gerar_id_produto(),
        "nome": nome_produto,
        "preco": float(preco_produto)}

    lista_produtos.append(produto)

    print(lista_produtos)

def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=id, reverse=True) #reverse com True aqui está invertendo a ordem da lista, iniciando pelo último
    
    novo_id = lista_produtos[0].get("id") + 1 #index 0, nesse caso, é o último item da lista já que a ordem está invertida
    
    return novo_id

def atualizar_produto():
    id_produto = input("Digite o ID do produto para atualizar: ")
    
    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("id") == int(id_produto):
            novo_valor = input("digite o novo valor do produto: ")
            lista_produtos[index]["preço"] = novo_valor
            print(f"\n PRODUTO ATUALIZADO COM SUCESSO! {lista_produtos[index]}")

def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"\n {lista_produtos[index]} \n")



menu()

