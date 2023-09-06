#Quero opção de:
#CRUD
#Adicionar doce
#Ler doce
#Atualizar doce
#Apagar doce
#Exibir a lista de todos os doces

import time

#lista que não está armazenando valores, esse eu coloquei manualmente, mas percebi que os valores que coloco só fica no terminal
lista_produtos = [{'id': 1, 'nome': 'mor', 'preço': 8.0}]

id_produto_del = 'id'

id_produto = 1

#função de menu sendo repetida diversas vezes pelo while, direcionando o usuario para cada opção que ele deseja
def menu():
    while True:
        print("/n ** MENU LOJA REPROGRAMA **")
        print("1 - Adicionar")
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")

        opcao = input("Escolha a opção desejada\n")

        print(opcao)

#ifs que dão as opções para direcionar o usuario de forma numeria para cada função a ser executada
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
        else:
            print("Opção inválida, por favor escolha uma opção do menu. :)")

    
     #As ações do programa       

#Gerador de ID por ordem crescente, começando do numero 1.
def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_produtos[0].get("id") + 1

    return novo_id

#Adiciona os produtos e mostra as especificações que o usuário precisa preencher
def adicionar_produto():
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = input("Digite o preço do produto:\n")

    produto = {
        "id": gerar_id_produto(),
        "nome": nome_produto,
        "preço": float(preco_produto),
    }
    lista_produtos.append(produto)

    print(lista_produtos)

#Estou com muita dificuldade em fazer a função funcionar, não sei o que acontece que parece que ela não conversa com o "if" de lá de cima, nunca funciona de primeira.
def exibir_detalhes():
    nome_produto = input("Digite o nome do produto:\n")
    
    for index in range(len('nome')):
        print(f"{lista_produtos['nome']}\n")



#Função que localiza o item de o acordo com a chave especifica 'id' e localiza na lista substituindo por outro input.
def atualizar_produto():
    id_produto = input("Digite o ID do produto para atualizar:\n")

    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("id") == int(id_produto):
            novo_valor = input("Digite o novo valor do produto:\n")
            lista_produtos[index]["preço"] = float(novo_valor)
            print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")


#Função que deleta valores da lista. Não consegui escrever mensagens de erro e exluir o item correto, tentei e pesquisei os tipos mais comuns de deletar item da lista,
#mas sem sucesso, a minha lista não armazena valores.

def deletar_produto():
    id_produto_del = input("Digite o ID do produto que quer excluir:\n")

    lista_produtos.remove(id_produto_del == 'id:\n')
    print(f"O produto foi deletado com sucesso!")

#Exibi a lista toda, com todos os produtos armazenados.
def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")

#inseri o menu novamente, mostrando todas a s opções.
menu()
