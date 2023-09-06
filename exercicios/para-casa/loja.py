#crud
#criar(criate) ler(read) atualizar(update) e deletar(delet) 
# quero poção de: criar doce
#listar doces
#atualizaer doces
#exir detalhes de um doce
#exibir lista todos os doces 
#apagar doces


lista_produtos = [] # lista vazia inicialmente ela não contém nenhum Produto. 
# Essa lista pode ser usada para armazenar elementos, como valores, objetos ou outros tipos de dados.


def menu():  # criação da função MENU. Aqui exibe as opções do sistema da Luja da may (o nome tem que mostrar o que faz
    while True: # loop para voltar ao menu e realizar novas interações com o sistema
        
        print ( "\n Bem vindes! Esse é  o Sistma de loja,  Doce Alegria. Utilise o menu e escolha a opção dejada \n ")
        print("\n ** MENU LOJA MAY DOCINHOS ** \n" )
        print(" 1 - Adicionar Produto " )
        print(" 2-  Exibir detalhes do Produto " )
        print(" 3 - Atualizar Produto " )
        print(" 4 - Excluir Produto  " )
        print(" 5 - Exibir todos os Produtos  " )
        print(" 0 - Sair do Sistema  \n" )
        
        opcao = input( " \n Escolha a opção desejada \n" ) # opção é digitada pela Usuária, elas escolhre dente as numerações acima
    # se não vai fazer operações usa string(retrno original
    #craição das condicionais para escolher a opção no menu, chamando as funçãoes definidas abaixo
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            exibir_detalhes()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            excluir_produto()
        elif opcao == "5":
            exibir_todos()
        elif opcao == "0":
            print ( " Sair ")    
        else:
            print( "\n Opção invalida! Por favor, Escolha uma opção do Menu\n")        
   
  #Funão adicionar_produto: adiciona novos produtos ao sistema ou reponhe estoque             
        
def adicionar_produto():
        nome_produto = input( " \nDigite o nome do produto\n") # a usuária digita 
        preco_produto = input( " \nDigite o preço do produto\n") # a usuária digita 
       # dicionário atributos caracteriticas
        produto = { "id": gerar_id_produto(),"nome": nome_produto, "preço ": float(preco_produto)}
            #chave: id, nome, preço
            
        lista_produtos.append(produto) # adiciona um produto  ao final da lista, atraves o método "append()"
        print (lista_produtos) # mostra a lista dos produtos adicionados na tela
        
        
        
   #Função gerar_id_produto: gera identificadores(códigos) para cada produto adicionado ao sistema        
def gerar_id_produto():
    if len(lista_produtos) == 0: # condional paraa checar se o tamnho da lista de produtos começa em zero
        return 1 # retorna 1 
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True) # inverter a lista para pegar o ultimo item
    novo_id = lista_produtos[0].get("id") + 1
    return novo_id
        # permite encontrar o que você quer 
        #print( lista_produtos[0].get( "id"))
        
        
     #Função Atualizar_produto: atualiza produtos do estoque adicionados ao sistema              
def atualizar_produto():
    id_produto = input("Digite o id do produto para atualizar:\n") # a Usuária digita
    
    for index in range (len(lista_produtos)): # percorre a lista para achar o id a ser atualizado
        if lista_produtos[index].get("id") == int(id_produto): # condional pega a id do produto selecionado
            novo_valor = input(" Digite o novo valor do produto:\n") # a usuária digita
            lista_produtos[index]["preço"] = float(novo_valor) # a usuária digita
            print (f" O produto foi atualizado com sucesso! {lista_produtos[index]}") # produto encontrado e atualizado mostra na tela
        else:
           print("Produto não encontrado. Digite uma Id válida")    # produto não encontrado
 
  # Função exibir_todos: exibe todos os  produtos cadastrados no sistema   
def exibir_todos():
    for index in range(len(lista_produtos)): # perceorre a lista 
        print(f"{lista_produtos[index]}\n")  # exibe toda lista na tela    
        
 # Função excluir_produto: exclue produto  cadastrado no sistema   
def excluir_produto():
    id_produto = input("Digite o id do produto para excluir:\n") # a usuária digita
    
    for index in range (len(lista_produtos)): # percorre a lista 
        if lista_produtos[index].get("id") == int(id_produto): # condional para selecionar o id 
           produto_excluido = lista_produtos.pop(index) # a função pop excule o produto do id selecionado
           print (f" o produto foi excluido com sucesso! {produto_excluido}") # mostra o produto excluido na tela
           break
        else:
         print("Produto não encontrado. Digite uma Id válida")   # produto não encontrado
 
 
  # Função exbir_detalhes: exibe detalhes individuais do produto selecionado  no sistema   
def exibir_detalhes():
    id_produto = input("Digite o ID do produto a ser exibido:\n") # a usuária digita

    for index in range(len(lista_produtos)): # percorre a lista
        if lista_produtos[index].get("id") == int(id_produto): # condional para pegar o id selecionado pela usuária
            produto = lista_produtos[index]  # Pega o produto selecionado
            print("Detalhes do produto:") # mostra os detalhes do produto selecionado. 
            for chave, valor in produto.items(): # percorre o id, valor do produto. O método .items() retorna uma lista de pares chave-valor, 
            #onde cada par é representado como uma tupla(imutável).
                print(f"{chave}: {valor}") # mostra os detalhes na tela 
            break
    else:
        print("Produto não encontrado.Digite uma Id válida") # senão encontrar o produto

            
menu()   # chama a Função menu novamente pelo loop while


