# Quero opção de:
# Adicionar doce
# Exibir detalhe de um doce
# Listar doces
# Atualizar doce
# Apagar doce
# Exibir a lista de todos os doces
lista_doces = [] #estrutura de dados tipo lista
                 # ela será nosso objeto iterável dentro do sistema
                 # todas as ações realizadas pelo usuário será baseado nessa lista
    
def menu(): #essa função eu deixei com esse nome mesmo porque faz muito sentido
    while True: # ela está nesse loop porque sempre irá aparecer pro cliente a cada vez que for aberto o sistema
        print ("\n ** MENU LOJA REPROGRAMA**\n")
        print (" 1- Adicionar")
        print (" 2- Buscar")
        print (" 3- Listar")
        print (" 4- Atualizar")
        print (" 5- Apagar")
        print (" 0- Sair")
        
        opcao_menu = input("Escolha uma função do Menu para realizar: \n") #pede uma entrada ao usuário referente as funcionalidades do menu que ele irá realizar.
        # estrutura condicional if/elif/else que percorre o menu e será
        #executado a partir do que o usuário escolher. (Mudei para opção Menu, para fazer referência ao Menu dentro do Código)
        if opcao_menu == "1":
            adicionar_doce()
        elif opcao_menu == "2":
            buscar_produto()
        elif opcao_menu == "3":
            listar_todos_doces()
        elif opcao_menu == "4":
            atualizar_doces()   
        elif opcao_menu == "5":
            excluir_doces()    
        elif opcao_menu == "0":
            break
        else:
            print("Opção inválida")
     #função adicionar_doce- é chamada quando o usuário seleciona a opção 1 no Menu
     # a função adiciona um novo cadastro de um doce a lista principal de todos os doces cadastrados no sistema  
def adicionar_doce(): # troquei todos os nomes das variáveis dentro dessa função para doce no final, para fazer referência ao produto vendido na loja
    nome_do_doce = input("Digite o nome do doce que você quer cadastrar:\n")
    preco_do_doce = input("Digite o preço do doce que você quer cadastrar:\n ")
    # a variável doce é composta pelos atributos que o objeto doce tem dentro da lista
    #que são: seu id, seu nome e preço. O id é gerado pelo sistema por questão de segurança
    # e ele é chamado pela sua função (gerar_id_doce_cadastrado)
    doce = { "id": gerar_id_doce_cadastrado(),"nome": nome_do_doce,"preço":float(preco_do_doce)}
    #função append- utilizada para adicionar a lista de doces principal mais um novo cadastro de um doce
    lista_doces.append(doce)
    print (lista_doces)
    #função complementar para quando for selecionada a opção 1 do menu pelo usuário
    #ela faz com que eseja gerado um id automático pelo sistema
    #o id é gerado a partir do último existente e de maior valor + 1. 
    # aqui foi utilizado o método sort + reverse - que inverte a posição dos id do maior para o menor
    #dessa forma quando se é criado um id novo ele vai para o início da lista 
    # então quando a função é chamada esse último id + 1 se torna o id mais recente 
    #gerado pelo sistema
def gerar_id_doce_cadastrado():
    if len(lista_doces)==0:
        return 1
    lista_doces.sort(key=id, reverse=True)
    
    novo_id = lista_doces[0].get("id")+1
    return(novo_id)
    # função atualizar_doce é chamada através do menu pela opção 4
    # está função é responsável por perguntar ao usuário qual item de sua lista principal
    #ele quer atualizar o atributo preço, deste item. 
    #selecionando através do método get() o sistema pede ao usuário qual o valor que ele quer inserir que 
    #passará a ser o novo  preço para o item. 
    #após isso através do id_produto que é o item escolhido pelo usuário para ser modificado
    #o sistema guarda o valor que ele quer substituir na variável novo_valor
    # e então ele sobrescreve o valor antigo pelo novo quando ele iguala
    #o valor selecionado para a mudança com a variável novo_valor
    #após isso é chamada a função print, mostrando o item que foi mudado na lista principal
    
def atualizar_doces():
    id_produto = input ("Digite o ID do doce que você quer atualizar: \n")
    for index in range(len(lista_doces)):
        if lista_doces[index].get("id")== int(id_produto):
            novo_valor = input("Digite o valor  que você quer atualizar:\n")
            lista_doces[index]["preço"] = float(novo_valor)
            print(f"Doce atualizado com sucesso {lista_doces[index]}")
#Função listar_todos_doces - é chamada quando o usuário escolhe a opção 3 do menu
#a função basicamente exibe toda a lista com todos os itens cadastrados pelo usuário.
#ela lê o tamanho inteiro da lista através do laço for dentro de uma range
# depois exibe toda a lista e todos os itens cadastrados nela.
def listar_todos_doces():
    for index in range(len(lista_doces)):
        print(f"{lista_doces[index]}\n")
#função excluir_doces é chamada através da opção 5 do menu
# com essa função o sistema permite ao usuário que ele exclua qualquer item da lista principal
#através do seu id, que é único dentro de todos os itens, o id é o único atributo que não se reprete
#entre todos os doces cadastrados na lista
# a função pede que o usuário informe o id do item para ser excluído e depois
# depois de informado o laço for procura através do índice dentro da listA_doces
# e com o método get() selecionada o atributo id desse index. 
# Compara o valor do index ao valor que o usuário digitou. Se for igual os dois
# a função exclui atravel do método del(), esse item da lista principal.  
# depois exibe a lista principal atualizada.    
def excluir_doces():
    id_produto_del = int(input("Digite o ID do doce que você quer excluir: \n"))
    for index in range(len(lista_doces)):
        if lista_doces[index].get("id")== int(id_produto_del):
            del (lista_doces[index])
            
            
        print("Doce Removido com Sucesso ",lista_doces)
# a função buscar_doce é chamada através da opção 2 do menu
# o usuário pode utilizar ela para buscar dados de um item específico que está cadastrado
#na lista principal.
#o usuário digita o id do produto e através do id o sistema faz a leitura no laço for
#percorre toda a lista principal, após isso compara dentro da condição if o valor que o usuário 
#digitou  a o índice do doce na lista principal, que no caso é pelo atributo id
# então a condição if traz que se este índice("id") for igual ao valor digitado pelo usuário
# ele mostra para o usuário somente aquele produto que ele buscou através
# do comando print (lista_doces[index]).
def buscar_produto():
    id_produto_busca = int(input("Digite o ID do doce que você quer buscar: \n"))
    for index in range(len(lista_doces)):
        if lista_doces[index].get("id")== int(id_produto_busca):
            print ("O doce que você buscou foi:" , lista_doces[index])
#função menu sendo chamada  no final do código para toda vez que for realizada uma função
# o menu seja exibido novamente para a realização de outra função
# caso o usuário não queira fazer mais nenhuma funcionadlidade no sistema 
#ele pode optar pelo 0 no menu principal, que leva ao encerramento do sistema.    
menu()