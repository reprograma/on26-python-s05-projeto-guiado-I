# CRUD - CRIAR -LER - .... - DELETAR
#quero opção de doce:
#adicionar doce
#exibir delhalhe de um doce
#atualizar doce
##apagar doces
#exibir a lista de todos os doces

lista_produtos = []

def menu():
    while True:
        print("\n ** MENU LOJA REPROGRAMA **\n")
        print("1 - Adicionar")
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")

        opcao =  input("Escolha a opção desejada:\n")
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            print("opção exibir detalhes doce")
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            print("opção apagar doce")
        elif opcao == "5":
            listar_todos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida, por favor escolha uma opção do menu")

def adicionar_produto():
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = float(input("Digite o preço do produto:\n"))

    produto ={"id": gerar_id_produto(), "nome": nome_produto,"preço": preco_produto}
    
    lista_produtos.append(produto)
    print(lista_produtos)

def  gerar_id_produto ():
    if  len ( lista_produtos ) ==  0 :
        return  1
    lista_produtos . sort ( key = lambda  produto : produto . get ( "id" ), reverso = True )
    novo_id  =  lista_produtos [ 0 ]. obter ( "id" ) +  1

    return  novo_id

def atualizar_produto():
    id_produto = input("Digite o ID do produto para atualizar:\n")
    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("") == int(id_produto):
            novo_valor = input("Digite o novo valor do produto: \n")
            lista_produtos[index]["preço"] = novo_valor
            print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")
            
def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")
menu()