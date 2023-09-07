# Quero opção de:
# Adicionar doce
# Exibir detalhe de um doce
# Atualizar doce
# Apagar doces
# Exibir a lista de todos os doces

#apaguei a biblioteca do import time, pois ela não estava sendo usada.

#lista_produtos é uma variavel que armazena uma lista de  dicionários, com as informações dos proodutos. Deixei o mesmo nome porque ele faz sentido no contexto.
lista_produtos = [{'id': 3, 'nome': 'asdasdas', 'preço': 32.0}, {'id': 2, 'nome': 'asd', 'preço': 2.0}, {'id': 1, 'nome': 'a', 'preço': 1.0}, {'id': 4, 'nome': '23123', 'preço': 13123.0}]

#id_produto é uma variavel que recebe o numero 1 que é por onde começamos o id em vez de 0, e deixei o mesmo nome. 
id_produto = 1
def menu():
    """
    Esta função menu representa o menu da loja, oferecendo diversas opções para o usuário interagir com a loja. 
    Ela exibe a numeração das opções,
    e quando o usuário seleciona uma opção, ela chama outra função que executará.
    :primeiro while - o loop, mostrar quais são as opções.
    :opcao que é uma variavel que receber o valor para comparar nas condicionais
    """
    while True:
        print("\n ** MENU LOJA REPROGRAMA **\n")
        print("1 - Adicionar")
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")

# Tratamento para aceitar apenas números inteiros como opções do menu.
# Enquanto a opção não for um número inteiro, o programa continuará pedindo uma escolha válida.
        while True: 
            try:
                opcao = int(input("Escolha a opção desejada\n"))
                break #Sair do loop se a conversão der certo
            except ValueError:#Lida com situações em que um valor inadequado é encontrado
                print("Por favor, digite um valor númerico válido para o preço.")

#Condições que determinam a ação desejada pelo usuário, retornando as outras funções
#deixei como foi passado acrecento as funções que estavam faltando, pois o restante fazia sentido
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            exibir_produtos()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            apagar_produto()
        elif opcao == "5":
            listar_todos()
        elif opcao == "0":
            break #Sair do loop do menu.
        else:
            print("Opção inválida, por favor escolha uma opção do menu")


def gerar_id_produto():
    """
    Esta função gera um novo ID para um produto com base na lista de produtos existente.
    Se a lista de produtos estiver vazia, o ID 1 é retornado(como mostra lá em cima).
    Caso contrário, a função ordena a lista de produtos com base nos IDs em ordem decrescente(reverse=True),
    obtém o ID do primeiro produto (o maior ID) e incrementa em 1 para criar um novo ID único.
    O novo ID gerado é, então, retornado.
    método .sort() para realizar a ordenação diretamente na lista original.
    """
    if len(lista_produtos) == 0: #verifica o tamanho de lista_produtos
        return 1 #se for 0 retorna 1
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)#key=lambda produto: produto.get("id"): Isso define uma função lambda que é usada como chave de ordenação. A função lambda recebe cada elemento produto da lista e retorna o valor associado à chave "id" de cada dicionário.
    novo_id = lista_produtos[0].get("id") + 1# ele pega o ID do primeiro produto na lista e incrementa 1 para criar um novo ID exclusivo para o próximo produto.
    return novo_id #restorna o novo id

def adicionar_produto():
    """
    Esta função permite ao usuário adicionar um novo produto à lista de produtos da loja.
    Solicita o nome e o preço do produto, garantindo que o preço seja um valor numérico válido.
    Gera um novo ID para o produto e adiciona o produto à lista de produtos existente.
    """
    nome_produto = input("Digite o nome do produto:\n")
# Tratamento para aceitar apenas números float como opções do menu.
# Enquanto a opção não for um float, o programa continuará pedindo uma escolha válida.
    while True:
        try:
            preco_produto = float(input("Digite o preço do produto:\n"))
            break#Sair do loop se a conversão der certo
        except ValueError:#Lida com situações em que um valor inadequado é encontrado
            print("Por favor, digite um valor númerico válido para o preço.")

#produto é uma variavel que armazena um dicionário, com as informações do novo prooduto.
    produto = {
        "id": gerar_id_produto(),#função que gera um novo id
        "nome": nome_produto,
        "preço": preco_produto, #tirei o float, pois ele está na parte de cima, no qual a pessoa é obrigada a colocar um valor float

    }
    lista_produtos.append(produto)#adiona a informação do novo produto na variavel lista de produtos
    
    print(lista_produtos)#imprimir toda a lista, até com os novos produtos adicionados.
    
def exibir_produtos():
    """
    Esta função permite ao usuário exibir detalhes de um produto com base no seu ID.
    Solicita o ID do produto, garantindo que seja um valor numérico válido.
    Em seguida, busca o produto na lista de produtos e exibe seus detalhes se encontrado.
    Caso contrário, exibe uma mensagem indicando que o produto não foi encontrado.
    """
    encontrado = False  # Inicialize a variável de controle como False, para que não imprima "não encotrado", quando estiver buscando o "id" do produto.
# Tratamento para aceitar apenas números inteiros como opções do ID.
# Enquanto a opção não for um número inteiro, o programa continuará pedindo uma escolha válida.
    while True:
        try:
            id_recebido = int(input("Qual é o ID do produto?\n"))
            break#Sair do loop se a conversão der certo
        except ValueError:#Lida com situações em que um valor inadequado é encontrado
            print("Por favor, digite um valor númerico válido para o ID.")
            
    for produto in lista_produtos:# Este loop itera por cada produto na lista de produtos.
        if produto["id"] == id_recebido: # Verifica se o ID do produto atual na iteração é igual ao ID recebido pelo usuário.
            print("Detalhes do Produto:")
            print(f"ID: {produto['id']}")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preço']:.2f}")
            encontrado = True  # Defina a variável de controle como True quando o produto é encontrado
            break#Sair do loop assim que produto é encontrado e impresso
        
    if not encontrado:#  # Se a variável 'encontrado' for False, significa que o produto não foi encontrado na lista.
        print("Produto não encontrado")#imprimir produto não encontrado


def atualizar_produto():
    """
    Esta função permite ao usuário atualizar o preço de um produto com base no seu ID.
    Solicita o ID do produto a ser atualizado.
    Em seguida, solicita o novo valor do preço, garantindo que seja um valor numérico válido.
    Atualiza o preço do produto na lista se o ID for encontrado e exibe uma mensagem de sucesso.
    Se o ID não for encontrado ou se a entrada for inválida, exibe uma mensagem apropriada.
    """
    id_produto = input("Digite o ID do produto para atualizar:\n")
    for index in range(len(lista_produtos)):#ele vai entrar no loop e vai percorrer pelo tamanho da lista
        if lista_produtos[index].get("id") == int(id_produto):# Verifica se o ID do produto na lista é igual ao ID fornecido pelo usuário. Se os IDs forem iguais, isso significa que o produto foi encontrado na lista.
            while True:# Entra em um loop infinito para solicitar ao usuário um novo valor para o preço do produto.      
                try:# Tenta converter a entrada do usuário em um número decimal (float).
                    novo_valor = float(input("Digite o novo valor do produto:\n"))# Se a conversão for bem-sucedida, o novo valor é atribuído à variável 'novo_valor'.
                    lista_produtos[index]["preço"] = novo_valor #tirei o float, pois ele já está sendo obrigado a arrumar ali em cima
                    print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")
                    break #Sair do loop se a conversão estiver correta
                except ValueError:
                    print("Por favor, digite um valor númerico válido para o novo preço")
                break#Sair do loop assim que a condição de cima for satisfeita
        else:
            print("Produto não encontrado.")  # Exibe mensagem se o ID do produto não for encontrado na lista.


def apagar_produto():
    """
    Função que permite apagar um produto da lista com base no seu ID.
    Solicita o ID do produto a ser apagado.
    Procura o produto na lista e o remove se encontrado.
    Exibe uma mensagem de sucesso se o produto for apagado.
    Se o ID não for encontrado, exibe uma mensagem informando que o produto não foi encontrado.
    """
    id_produto = input("Digite o ID do produto para apagar:\n")# Solicita o ID do produto a ser apagado.
    for produto in lista_produtos:
        if produto["id"] == int(id_produto): # Verifica se o ID do produto atual é igual ao ID fornecido pelo usuário.
            lista_produtos.remove(produto) # Remove o produto da lista.
            print("O produto foi apagado com Sucesso.\n")  # Exibe uma mensagem de sucesso.
            break # Sai do loop para evitar a remoção de outros produtos com o mesmo ID.
    else:
        print("Produto não encontrado.") # Exibe uma mensagem se o produto não for encontrado na lista.


def listar_todos():
    """
    Função que lista todos os produtos da loja.
    Itera pela lista de produtos e exibe cada produto na tela.
    """
    for index in range(len(lista_produtos)):# Itera por cada índice na lista de produtos.
        print(f"{lista_produtos[index]}\n")  # Exibe as informações do produto atual seguidas de uma quebra de linha.

menu()
# Chama a função 'menu' para exibir o menu da loja e permitir que o usuário interaja com as opções disponíveis.