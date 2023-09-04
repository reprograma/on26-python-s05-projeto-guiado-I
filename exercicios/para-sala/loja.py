#qr no menu:
    #adicionar doce
    #exibir detalhes de 1 doce
    #atualizar doce
    #apagar doces
    #exibir lista de todos os doces


#criar uma variavel chamada de lista produtos e quando chamarmos o : 
lista_prod = [
    #{"id": 2, "nome": "Novo produto2", "preço": 3.0},
    #{"id": 3, "nome": "Novo produto3", "preço": 7.0},
    #{"id": 1, "nome": "Novo produto", "preço": 9.0},
]

def menu_loja():
    while True:
        print("\n ** MENU LOJA {reprograma} ** \n")
        print("\n 1 - Adicionar")
        print("\n 2 - Exibir detalhes")
        print("\n 3 - Atualizar")
        print("\n 4 - Apagar")
        print("\n 5 - Exibir lista completa")
        print("\n 0 - Sair \n")

        opcao = int(input("Coloque aqui a opção desejada: \n"))

        if opcao == 1:
            adic_prod()
        elif opcao == 2: 
            print("Opção exibir detalhes do doce ")
        elif opcao == 3: 
            atualizar_prod()
        elif opcao == 4: 
            print("Opção apagar doce")
        elif opcao == 5: 
            print("Opção exibir lista completa de doces")
        elif opcao == 0: 
            break
        else: 
            print("Indicar uma opção válida, por favor")


def adic_prod():
    nome_prod =  input("Qual o nome do doce que deseja adicionar? \n ")
    preco_prod =  float(input("Qual o preço do doce que deseja adicionar? \n "))
    produto = {
        "id" : gerar_id_produto(),
        "nome" : nome_prod,
        "preço" : preco_prod
    }

    lista_prod.append(produto)

    print(lista_prod)

def gerar_id_produto():
    if len(lista_prod) == 0:
        return 1
    #quem ela quer ordenar, a chave que ela vai ser ordenada é o id, e usamos o reverse true para ele ordenar do maior para o menor(se deixasse false, ela seria ordenada do menor para o maior). 
    lista_prod.sort(key = id, reverse = True)
    novo_id = lista_prod[0].get("id") + 1
                            #onde iremos pegar o valor do id, se quisermos o nome colocaríamos ali entre aspas o nome. 
    return novo_id

def atualizar_prod():
    id_produto = input("Digite o ID do produto para atualizar: \n")

menu_loja()