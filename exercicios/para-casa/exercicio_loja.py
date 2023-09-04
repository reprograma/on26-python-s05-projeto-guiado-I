#Criar um menu para as clientes

    #*ANTES DE TUDO, CRIAR UM MENU COM DOCES QUE TERÁ NA LOJA*

    #Escolher produto e adicionar ele num carrinho 
    #Esse produto tem que ser escolhido pelo seu identificador, ex: se o brigadeiro tiver o id 2 a cliente tem que colocar no carrinho 2
    #Escolher a quantidade desejada. 
    #Se o cliente mudar de ideia ele pode excluir do carrinho
    #O cliente poderá ver o valor total dos itens a qualquer momento. 
    #Quando o cliente finalizar, deverá aparecer o total de quantidade e o total valor.

#Criar um menu que se for o 1, chamar a loja do cliente. Se for o 2 falar que só está disponível para pessoas autorizadas.

carrinho = [] #Colocar essa lista vazia para quando os clientes forem adicionando os produtos no carrinho ele venha ser colocado nesse lista. 

def mostrar_menu_inicial(): 
    
        print("** MENU **")
        print("1 - Sou cliente")
        print("2 - Sou funcionário")
        print("0 - Sair")

        opcao = int(input("Coloque o valor escolhido: "))
        if opcao == 1: 
            menu_cliente()
        elif opcao == 2: 
            print("Essa opção só está disponível com autorização.")
        

def menu_cliente(): 
    while True:
        print("** Menu Doces da May **")
        print("1 - Brigadeiro Tradicional")
        print("2 - Brigadeiro de Oreo")
        print("3 - Beijinho")
        print("4 - Bolo de Rolo")
        print("5 - Pudim de Leite Condensado")
        print("6 - Cocada")
        print("7 - Goiabada")

        escolha1 = int(input("Escolha qual opção deseja do nosso cardápio, por favor informar apenas o número!"))
        quantidade1 = int(input("Escolha a quantidade que deseja, pedimos desculpas pelo incoviniente mas apenas vendemos eles inteiro."))
        

        produtos = [ 
            {"ID" : 1, "Nome": "Brigaderio Tradicional", "Preço" : 2.5}, 
            {"ID" : 2, "Nome" : "Brigadeiro de Oreo", "Preço" :  3.0},
            {"ID" : 3, "Nome" : "Beijinho", "Preço" :  3.0},
            {"ID" : 4, "Nome" : " Bolo de Rolo", "Preço" :  6.0},
            {"ID" : 5, "Nome" : " Pudim de Leite Condensado", "Preço" :  5.0},
            {"ID" : 6, "Nome" : " Cocada", "Preço" :  4.0},
            {"ID" : 7, "Nome" : " Goiabada", "Preço" :  4.0}
        ]
    
        if escolha1 == 1:
            print(produtos[0])
        elif escolha1 == 2: 
            print(produtos[1])
        elif escolha1 == 3: 
            print(produtos[2])
        elif escolha1 == 4: 
            print(produtos[3])
        elif escolha1 == 5: 
            print(produtos[4])
        elif escolha1 == 6: 
            print(produtos[5])
        elif escolha1 == 7: 
            print(produtos[6])
        else: 
            print("Por favor, escolha uma opção válida.")
            break
            
    
    
    
    

mostrar_menu_inicial()