#Quero opção de:
#Adicionar doce
#Exibir doce
#atualizar doces
#Apagar doces
#Existir lista de todos os doces

# **************************         [A] - lista_produtos  **************************  

# *Iniciamos o programa com a lista_produtos, que é o ambiente em que vai listar o "id, preço e detalhes" realtivos ao produto.
#______________________________________________________________________________________________________________________________________________________________

#[A]

lista_produtos = [{'id': 1, 'nome': 'Brigadeiro', 'Preço': 3.0, 'detalhes': 'Brigadeiro: Chocolate, leite condensado, manteiga, Granulado e Leite'},
 {'id': 2, 'nome': 'Sonho', 'Preço': 5.0, 'detalhes': 'Sonho: farinha de trigo, açucar, fermento, leite, goaibada e ovos'},
 {'id': 3, 'nome': 'Beijinho', 'Preço': 3.0, 'detalhes': 'Beijinho: Leite condensado, manteiga, coco e leite'}]


# **************************         [B] - def menu()      **************************  

# * Está a função responsável pelas opções do menu da loja;
# * O "while true" nesta função significa que a função "def menu()" vai funcionar em um loop infinto até que a opção (que no caso é a opção 0) seja solicitada,
#causando assim  a interrupção do menu de opções, do contrário poderemos tanto adcionar produtos e utilizar todas as outras funcionalidades do menu, 
#que ficaram armazenadas enquanto o programa estiver sendo utilizado pelo usuário;
# * Os condicionantes "if, elif e else" são as possibilidades oferecidas no menu de opções;
# *Nas opções [1] até a a [5], temos várias "def ...()"", que são as funções que foram definidas logo abaixo para dar funcionalidades ao menu;
# * A opção [0], como dito antes, tem a função "break", que serve como ponto de parada do programa.
#______________________________________________________________________________________________________________________________________________________________

#[B]

def menu():
    while True:
        print("\n **Menu Loja Reprograma**\n")
        print("1 - Adicionar doces")
        print("2 - Exibir detalhes dos doces")
        print("3 - Atualizar doces")
        print("4 - Apagar doces")
        print("5 - Exibir todos os doces")
        print("0 - Sair \n")

        opcao = int(input("Escolha o número da opção desejada: \n"))
        if opcao == 1:
            adicionar_produto()
        elif opcao == 2:
            exibir_detalhes()
        elif opcao == 3:
            atualizar_produto()
        elif opcao == 4:
            apagar_produto()
        elif opcao == 5:
            exibir_todos_produtos()
        elif opcao == 0:
            print("Sair")
            break
        else:
            print("Opção inválida, por favor escolha uma opção do menu")

# **************************         [C] - def gerar_id_produtos()    **************************  

# *Está função é responsável pela criação do "id" (identificação em códico numérico) de cada produto, de modo que cada produto tenha uma "id" diferente e que, 
#neste caso,#seguirá uma progressão de razão 1, iniciando do 1;
# * O "if len(lista_produtos) == 0," significa que teremos uma lista de produtos iniada em vazio e o "return 1" deve ser considerada o valor 1 #de um primeiro 
#intem da lista;#
# * O "lista_produtos.sort" é utilizada para ordenar a lista_produtos em ordem crescente;#
# * Dentro de "lista_produto.sort()" tem a "Key", que é aplicada a cada elemento da sequência antes de serem comparados para determinar #a ordem de classificação,
#por isso ela é "=" a "lambda", que por sua vez desempenha a função de extrai o valor do campo "id" de cada #elemento da lista para ser usado como critério de 
#ordenação;
# * Em "novo_id = lista_produtos[0].get("id")+1" serve para que cada novo produto adcionado tenha um novo número "id", que será o número anterior acrescido de 1.
#__________________________________________________________________________________________________________________________________________________________________

#[C]

def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_produtos[0].get("id") + 1
    return novo_id

# **************************         [D] - def adicionar_produtos()    **************************  

# * Esta função está associada a opção [1] Adicionar Doces, assim que usuario solicitá-la vai ser a função que executarar os comandos a seguir;
# * Nesta função teremos os "inputs" em que o usuário vai adicionar: "nome_produto, preco_produto, detalhes_produtos";
# * Criaremos um dicionário "produto", com quatro opções "id, nome, preço e detalhes", que serão as atribuições que constará na lista_de_produtos, para cada item atribuido pelo usuário;
# * Em lista_produtos.append(produtos), é o banco (lista) criada pelo usuário referente ao comando da descrição que vimos no início em [A], referente a lista _produtos;
# Por fim, a função vai printar o produto adciconado pelo cliente com sua "id, preço, nome e detalhes", acompanhado da mensagem "Produto adicionado com sucesso".
#________________________________________________________________________________________________________________________________________________________________________________________

#[D]

def adicionar_produto():
    nome_produto = input("Digite o nome do produto: \n")
    preco_produto = float(input("Digite o preço do produto: \n"))
    detalhes_produto = input("Digite o produto, seguido dos detalhes ou de sua composição: ")
    produto = {
        "id": gerar_id_produto(),
        "nome": nome_produto,
        "Preço": preco_produto,
        "detalhes": detalhes_produto
    }
    lista_produtos.append(produto)
    print(f"Produto adicionado com sucesso! {produto}")

# **************************         [E] - def exibir_detalhes()    **************************  

# * Está função vai mostrar os detalhes que foi adicionado na função [1], relativos a cada produto ou detalhes que já esteja na lista;
# * O "id_produto" é para o usuário digitar o id de um produto já adcionado;
# * Em "for produto in lista_produtos:",  ele busca o produto do dicionário "id" que será igual ao número id que o usuário digitou e sehuida ele vai printar a id e os detalhes
#do produto já adcionado pelo usuário, caso o usuário digite um número que ainda não tenha id ele printa que não foi encontrada aquele id.
#________________________________________________________________________________________________________________________________________________________________________________________

#[E]

def exibir_detalhes():
    id_produto = int(input("Digite o ID do produto para exibir detalhes: "))
    for produto in lista_produtos:
        if produto["id"] == id_produto:
            print(f"Detalhes do Produto {id_produto}: {produto['detalhes']}")
            return
    print(f"Produto com ID {id_produto} não encontrado.")

# **************************         [F] - def atualizar_produto()    **************************  

# * Esta função serve para atualizar os valores dos produtos que já estão na lista de produtos;
# * O "id_produto" como input, serve para o usuario digitar o id do produto que o usuário quer atualizar;
# * A finalidade do " for produto in lista_produtos",  determina que para os produtos em lista_produtos, onde o produto selecionado equivale a id já existente;
# * Em "novo_valor" o usuário vai digitar um novo valor ao produto selecionado pela id;
# * Em "produto[id] == id_produto" o usuário determina que o valor do produto solicitado pelo seu id será a ele atribuído o novo_valor recebido pelo usuário;
# * Printa no final o novo valor atribuído ou caso id não seja encontrado, sinaliza para o usuário.
#________________________________________________________________________________________________________________________________________________________________________________________

#[F]

def atualizar_produto():
    id_produto = int(input("Digite o ID do produto para atualizar: "))
    for produto in lista_produtos:
        if produto["id"] == id_produto:
            novo_valor = float(input("Digite o novo valor do produto: "))
            produto["Preço"] = novo_valor
            print(f"O produto foi atualizado com sucesso! {produto}")
            return
    print(f"Produto com ID {id_produto} não encontrado.")

# **************************         [G] - def apagar_produto()    **************************  

# * Está função vai retirar algum produto que já esteja na lista;
# * O "id_produto" vai pedir para que o aluno digite um núemro id de um produto existente na lista;
# * O "for produto in lista_produtos" vai colocar o produto[id] ser igual a ao "produto" da lista da id digitada pelo usuário;
# * Em seguida o produtoa que estão na lista de produto da id selecionada, a ser removido da lista através da função "lista_produto.remove(produto)";
# * Em seguida o programa vai printar o produto selecionado pela id que foi removido ou printar que não encontrou caso a id não tenha sido encontrada nos produtos da lista.
#________________________________________________________________________________________________________________________________________________________________________________________

#[G]

def apagar_produto():
    id_produto = int(input("Digite o ID do produto para apagar: "))
    for produto in lista_produtos:
        if produto["id"] == id_produto:
            lista_produtos.remove(produto)
            print(f"Produto com ID {id_produto} foi removido com sucesso.")
            return
    print(f"Produto com ID {id_produto} não encontrado.")

# **************************         [H] - def exibir_todos_produtos()    **************************  

# * Esta função está direcionada a exibição de todos os produtos da lista, tanto produtos que já estavam, quanto os que foram adicionados pelo usuário;
# * O "for produto in lista_produtos", define produto enquanto toda a lista e em seguida ele pede que faça o print com todas as epecificações que eles possuem na lista.
#________________________________________________________________________________________________________________________________________________________________________________________

#[H]

def exibir_todos_produtos():
    print("\nLista de Todos os Produtos:")
    for produto in lista_produtos:
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: {produto['Preço']}, Detalhes: {produto['detalhes']}")
    print("\n")

# **************************         [I] - menu()    **************************  

# * Esta linha chama a função "def menu ()" para ser executada.
#________________________________________________________________________________________________________________________________________________________________________________________

#[I]

menu()
