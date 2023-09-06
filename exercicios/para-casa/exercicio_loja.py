#Criar um menu para as clientes

    #*ANTES DE TUDO, CRIAR UM MENU COM DOCES QUE TERÁ NA LOJA* ok

    #Escolher produto e adicionar ele num carrinho 
    #Esse produto tem que ser escolhido pelo seu identificador, ex: se o brigadeiro tiver o id 2 a cliente tem que colocar no carrinho 2
    #Escolher a quantidade desejada. 
    #Se o cliente mudar de ideia ele pode excluir do carrinho
    #O cliente poderá ver o valor total dos itens a qualquer momento. 
    #Quando o cliente finalizar, deverá aparecer o total de quantidade e o total valor.

#Criar um menu que se for o 1, chamar a loja do cliente. Se for o 2 falar que só está disponível para pessoas autorizadas.


carrinho = []  # Lista vazia para armazenar os IDs dos produtos no carrinho

    #função para quando chamada mostrar o menu inicial
def mostrar_menu_inicial():
    print("* MENU *")
    print("1 - Sou cliente")
    print("2 - Sou funcionário")
    print("0 - Sair")

    opcao = int(input("Coloque o valor escolhido: "))
    if opcao == 1:
        menu_cliente()
    elif opcao == 2:
        print("Essa opção só está disponível com autorização.")
    elif opcao == 0:
        saida = int(input("Tem certeza que não vai dar uma olhadinha? Para Sim digite 1 e para Não digite 0, escreva aqui sua resposta: "))

        if saida == 1:
            mostrar_menu_inicial()
        elif saida == 0:
            exit("Obrigada por entrar em nossa loja online!")
        else: 
            print("Escolher uma opção válida")

    #função que abrirá um menu para mostrar as opções que o user pode escolher.
def menu_cliente():
    while True:
        print("* MENU *")
        print("1 - Mostrar cardápio")
        print("2 - Adicionar produto")
        print("3 - Mostrar carrinho")
        print("4 - Pagar o total da compra")
        print("0 - Voltar")

        opcao = int(input("Coloque o valor escolhido: \n"))

        if opcao == 1:
            mostrar_cardapio() #mostrará o cardápio com os produtos e o valor de cada.
        elif opcao == 2:
            adicionar_prod_carrinho() 
            #Mostrará de novo o cardápio para o user ter certeza o número do produto escolhido e adicionará tudo na lista vazia carrinho que criei lá em cima
        elif opcao == 3:
            mostrar_carrinho() 
            #Terá que mostrar o carrinho com tudo que estiver dentro da lista carrinho que serão os produtos que foram adicionados na função anterior.
        elif opcao == 4:
            pagar_carrinho() 
            #Mostrar o valor total da compra e finalizará o carrinho
        elif opcao == 0:
            #Caso não queria fazer nada
            print("Voltando para o menu inicial...")
            break
        else:
            print("Opção inválida, tente novamente!")

#criei uma função que mostre os produtos e dentro criei uma biblioteca, não sei se precisa criar um função para isso mas na minha cabeça precisa, pq descobrir que com a biblioteca consigo usar os ids de fora mais fácil kk na real pensando bem posso deixar so a bibliotela la fora né? ah vou deixar assim mesmo.
menu = {
    1: {"item": "Brigaderio Tradicional", "Preço": 2.5},
    2: {"item": "Brigadeiro de Oreo", "Preço": 3.0},
    3: {"item": "Beijinho", "Preço": 3.0},
    4: {"item": "Bolo de Rolo", "Preço": 6.0},
    5: {"item": "Pudim de Leite Condensado", "Preço": 5.0},
    6: {"item": "Cocada", "Preço": 4.0},
    7: {"item": "Goiabada", "Preço": 4.0}
}

#CRIAÇÃO DAS FUNÇÕES PARA CASA OPÇÃO. 

def mostrar_cardapio():
    print("\n** Cardápio **")
    for id, produto in menu.items():
        print(f"{id}:  {produto['item']} - R${produto['Preço']}")

def adicionar_prod_carrinho():
    mostrar_cardapio()
    num_produto = int(input("Digite o código do produto que deseja adicionar: \n"))
    if num_produto in menu:
        carrinho.append(num_produto)
        print(f"\nProduto {menu[num_produto]['item']} adicionado ao carrinho com sucesso!")
    else:
        print("Por favor, insira um número que pertença ao cardápio!")

def mostrar_carrinho():
    print("======================\n")
    if carrinho:
        print("\n ** Itens no carrinho **\n")
        total_compra = 0  # Inicialize o total
        for num_produto in carrinho:
            produto = menu[num_produto]
            print(f"{produto['item']} - R${produto['Preço']}")
            total_compra += produto['Preço']  # Adicione o preço ao total
        print(f"Total a ser pago: R${total_compra}")
    else:
        print("Carrinho vazio :( ")
    print("\n======================")

def pagar_carrinho():
    print("\n")
    mostrar_carrinho()  # Mostra o carrinho para o cliente
    print("Pagamento realizado com sucesso! Obrigado por sua compra.")
    carrinho.clear()  # Limpa o carrinho após o pagamento

mostrar_menu_inicial()