# Exercicio Tentando melhorar o código da Lojinha de doces Reprograma
# Estudante: Cristiane Pereira, prof: Manuelly Suzik

lista_produtos = []

# Achei melhor criar uma função para exibir as opções porque exibir toda vez me pareceu ruim de visualizar
def opcoes_menu():
    print("\n ** MENU LOJA REPROGRAMA ** \n")
    print("1 - Adicionar")
    print("2 - Exibir detalhes")
    print("3 - Atualizar")
    print("4 - Apagar")
    print("5 - Exibir todos")
    print("0 - Sair")

# Com as minhas mudanças, as opções do menu não vão aparecer toda vez que o menu for chamado, mas se o usuário quiser, elu pode selecionar a opção A para rever as opções
def menu():
    while True:
        opcao = input("\nMENU: Digite o número da opção desejada ou digite A para rever as opções: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            exibir_detalhes()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            apagar_produto()
        elif opcao == "5":
            listar_todos()
        elif opcao == "A" or opcao == "a": 
            opcoes_menu()
        elif opcao == "0": 
            break
        else:
            print("Opção inválida, por favor escolha uma opção do menu.")
    
# Como o código passado em aula estava dando erro na opção de criar id acima de 3 produtos, modifiquei o código do gerador, passando a utlizar a função de observar o tamanho da lista para pegar o último index criado. Também mantive o código na função de adicionar produto, porque não vejo razão para ter uma função separada para gerar o id, uma vez que só criamos novos ids quando novos produtos são adicionados. Também fiz o tratamento de erros para o caso do usuário digitar algo que não dá para converter para float em preço do produto. Por fim, adicionei a opção de voltar para o menu antes de terminar a ação utilizando o #. 
def adicionar_produto():
    print("\n<<OPÇÃO ADICIONAR PRODUTO>>")
    nome_produto = input("Digite o nome do produto ou # para retornar para o menu principal: ")
    if nome_produto != "#":
        preco_produto = input("Digite o preço do produto ou # para retornar para o menu principal: ")
        if preco_produto != "#":
            
            while type(preco_produto) == str:
                try:
                    preco_produto = float(preco_produto)
                except:
                    print("Digite apenas números.")
                    preco_produto = input("Digite o preço do produto novamente: ") #pensei em colocar aqui a opção de voltar para o menu, mas achei que teria que colocar muito código a mais, então se usuário quiser, ele pode apagar o produto depois.      

            novo_id = 1 #prefiro usar o 1 como valor default ao invés de fazer um if/else, não vejo como poderia dar problema

            if len(lista_produtos) > 0:
                tam_lista = len(lista_produtos)
                novo_id = lista_produtos[tam_lista-1].get("id")+1

            produto = {
                "id": novo_id,
                "nome": nome_produto,
                "preço": preco_produto
                }

            lista_produtos.append(produto)
            #print(lista_produtos) - Retirei a linha por achar que mostrar toda lista toda vez era ruim de visualizar, prefiro mostrar só o prod adicionado
            print(f"Produto adicionado com sucesso! Confira: {lista_produtos[-1]}") 
            

#Criei uma função para verificar se o id digitado pelo usuário existe, pois elu pode digitar um id que não tem na lista.
def autenticacao_id():
    id_usuario = input("Digite o id do produto ou # para retornar para o menu principal: ")

    if id_usuario != "#":
        status = "NDA"
        
        while type(id_usuario) == str:
            try:
                id_usuario = int(id_usuario)
            except:
                print("Digite apenas números.")
                id_usuario = input("Digite o id do produto novamente: ")

        for index in range(len(lista_produtos)):
            if lista_produtos[index].get("id") == int(id_usuario):
                status = "Produto encontrado"
        
        if status == "NDA":
            print("Não há produto com esse id na base de dados do programa, voltando ao menu principal.")
        else:
            return id_usuario

# Função solicitada de exibir detalhes
def exibir_detalhes():
    print("\n<<OPÇÃO EXIBIR DETALHES>>")
    id_produto = autenticacao_id()
    
    if id_produto != None and id_produto != "#":
        for item in range(len(lista_produtos)):
            if lista_produtos[item].get("id") == id_produto:
                print(lista_produtos[item])

# Adicionei a função de voltar ao menu e testo o valor do novo preço
def atualizar_produto():
    print("\n<<OPÇÃO ATUALIZAR PRODUTO>>")
    id_produto = autenticacao_id()
    
    if id_produto != None and id_produto != "#":
        for index in range(len(lista_produtos)):
            if lista_produtos[index].get("id") == int(id_produto):

                novo_valor = input("Digite o novo valor do produto: ")

                while type(novo_valor) == str:
                    try:
                        novo_valor = float(novo_valor)
                    except:
                        print("Digite apenas números.")
                        novo_valor = input("Digite o novo valor do produto: ")

                lista_produtos[index]["preço"] = novo_valor
                print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")

# Função solicitada de apagar produto, estava dando erro de index não existente por causa do for que continua com o tamanho da lista até o final mesmo após apagar um item, resolvi adicionando um if para testar tamanho da lista e index
def apagar_produto():
    print("\n<<OPÇÃO APAGAR PRODUTO>>")
    id_produto = autenticacao_id()
    
    if id_produto != None  and id_produto != "#":
        for item in range(len(lista_produtos)):
            if item < len(lista_produtos):
                if lista_produtos[item].get("id") == id_produto:
                    lista_produtos.pop(item)
                    print("O produto foi excluído com sucesso!")

#Não vejo razão de alterar a função de listar todos os produtos
def listar_todos():
    print("\n<<TODOS OS PRODUTOS CADASTRADOS>>")
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}")

opcoes_menu()
menu()