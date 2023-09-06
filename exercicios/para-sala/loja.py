#Quero opção de
#Adicionar doce
#Exibir detalhe de um doce
#Listar doce
#Atualizar doce

lista_produtos = []


def menu():
        while True:

            print("\n ** MENU LOJA REPROGRAMA ** \n")
            print("1 - Adicionar")
            print("2 - Exibir detalhes")
            print("3 - Atualizar")
            print("4 - Apagar")
            print("5 - Exibir todos")
            print("0 - Sair")
            
            opcao = input('Esolha a opção desejada\n')

            print(opcao)

            if opcao =="1":
                adicionar_produto()
            elif opcao =="2":
                print("opção exibir detalhes")
            elif opcao =='3':
                print('Atualizar')
            elif opcao =='4':
                print('Apagar')
            elif opcao =='5':
                print('Exibir todos')
            elif opcao =='0':
                  break
            
            else:print("Opção inválida,por favor escolha uma opção do menu ")


def adicionar_produto():
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = input("Digite o preço do produto:\n")

    produto = {
         "id":gerar_id_produto(),
         "nome":nome_produto,
         "preço": float(preco_produto)
         }

    lista_produtos.append(produto)
    
    print(lista_produtos)

def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=id, reverse=True)
    novo_id = lista_produtos[0].get("id")+1
    return novo_id

menu()