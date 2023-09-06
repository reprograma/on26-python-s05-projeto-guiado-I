# Quero a opção de:
# Adicionar doce
# Exibir detalhe de um doce
# Atualizar doce
# Apagar doces 
# Exibir lista de todos os doces
import time

lista_produtos = []

id_produto = 1

def menu():
    while True:
        print("\n ** MENU DA LOJA REPROGRAMA ** \n")
        print("1 - Adicionar")
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")

        opcao = input("\n Digite a opção desejada\n")
        
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            exibir_detalhes()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            apagar_doce()
        elif opcao == "5":
            listar_todos_os_produtos()
        elif opcao == "0":
            print("opcao sair")
            break
        else:
            print("\n Por favor, digite uma opção válida \n")

def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_produtos[0].get("id") + 1
    return novo_id

def adicionar_produto():
    nome_produto = input("Informe o nome do produto:\n")
    preco_produto = float(input("Informe o preço do produto:\n"))
    
    produto = {
        "id": gerar_id_produto(), 
        "nome": nome_produto, 
        "preço": float(preco_produto),
        }

    lista_produtos.append(produto) #ele pode estar adicionando o produto antes de fazer o role todo

    print(lista_produtos)

def exibir_detalhes():
    id_produto_escolhido = input("Digite o ID do produto a ser exibido: \n")
    for index in range(len(lista_produtos)):
        if int(id_produto_escolhido) == lista_produtos[index].get("id"):
            print(lista_produtos[index].get("nome"))
            

def atualizar_produto():
    id_produto = input("Digite o ID do produto para atualizar:\n")
    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("id") == int(id_produto):
            novo_valor = input("Digite o novo valor do produto:")
            lista_produtos[index]["preço"] = float(novo_valor)
            print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")

def apagar_doce():
    id_para_apagar = input("Informe o código do doce que será apagado: \n")
    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("id") == id_para_apagar:
            lista_produtos.pop(index)
            print("O produto foi apagado com sucesso")


    #if apagar_doce_por_id in lista_produtos:
    #    lista_produtos.remove(apagar_doce_por_id)
    #    print(lista_produtos)
    #else:
    #    print("Código do produto não encontrado. Favor digitar um código válido.")

def listar_todos_os_produtos():
    for index in range(len(lista_produtos)):
        print("f{lista_produtos[index]}\n")

    
menu()
    