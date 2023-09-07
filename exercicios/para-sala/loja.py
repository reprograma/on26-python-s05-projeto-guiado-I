# Quero opção de:
# Adicionar doce
# Exibir detalhe de um doce
# Atualizar doce
# Apagar doces

# Exibir a lista de todos os doces

# removi o import time 
lista_produtos = [{'id': 3, 'nome': 'asdasdas', 'preço': 32.0}, {'id': 2, 'nome': 'asd', 'preço': 2.0}, {'id': 1, 'nome': 'a', 'preço': 1.0}, {'id': 4, 'nome': '23123', 'preço': 13123.0}]

# Importante definir o identificador do produto, para garantir que cada produto tenha sua identificação para as demais funcionalidades
id_produto = 1
def menu():
    #Definir a função menu, para apresentar as demais funções do menu
    while True:
    # para um controle de repetição, em caso que seja usado repetidamente até uma codição de parada seja usada atéque seja interrompida.
        print("\n ** MENU LOJA REPROGRAMA **\n")
        print("1 - Adicionar")
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")


        opcao = input("Escolha a opção desejada\n")
        #interação para que o usuário interaja e "diga" a opção desejada
        #Cada função abaixo, apresenta uma opção do menu do menu e executa de acordo com a escolha do usuário.
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            exibir_detalhes()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            delete()
        elif opcao == "5":
            listar_todos()
        elif opcao == "0": 
            #BREAK, ncessario no caso em tela para 'quebrar', 'interromper', 'pausar' o loopig
            break
        else:
            print("Opção inválida, por favor escolha uma opção do menu")

def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    # será ultilizado .sort, é um método de lista que sera ultilizado para ordenar os elementos dessa lista. No caso em tela, está sendo usado para ordenar os produtos em `lista_produtos
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_produtos[0].get("id") + 1

    return novo_id
def adicionar_produto():
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = input("Digite o preço do produto:\n")

    produto = {
        "id": gerar_id_produto(),
        "nome": nome_produto,
        "preço": float(preco_produto),
    }
    #Deverá ser ultilizado append para adicionar ou "anexar" um elemento na lista_produtos.É o nome da lista à qual você deseja adicionar um elemento. A variável `lista_produtos` deve ser uma lista previamente definida em seu código. - `.append
    lista_produtos.append(produto)

    print(lista_produtos)



def atualizar_produto():
    id_produto = input("Digite o ID do produto para atualizar:\n")

    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("id") == int(id_produto):
            novo_valor = input("Digite o novo valor do produto:\n")
            lista_produtos[index]["preço"] = float(novo_valor)
            print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")


def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")

#exibir detalhes do menu
def exibir_detalhes():
    exibir_item = int(input("Digite a id:"))
    
    for index in lista_produtos:  
        if exibir_item == index.get("id"): 
           print(f"{index}")
      
def delete():
    deletar_produto = int(input("Digite id que deseja deletar:"))

    for index in range(len(lista_produtos)): 
        if index < len(lista_produtos):     
            if lista_produtos[index].get("id") == deletar_produto:
                lista_produtos.pop(index)   
                print("O produto foi excluído com sucesso!")
menu()

