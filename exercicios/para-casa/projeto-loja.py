# A cliente Mayhhara é uma pessoa bem criativa, ela teve a ideia de criar um sistema 
# para a sua lojinha de doces. Já que ela não sabe como implementar isso pois ela nunca 
# fez um curso da reprograma ela decide te chamar para fazer isso pra ela. Um sistema 
# simples vai servir, as únicas exigências que ela pede são:
#   - Deve ser escrito em python
#   - Deve conseguir adicionar doces novos ao menu
#   - Deve ser possível mostrar detalhes de um produto pelo seu IDENTIFICADOR
#   - Deve listar todos os itens do menu
#   - Deve ser possível ALTERAR O PREÇO de um certo protudo
#   - Deve apagar um produto do menu.

# Observações:
#   - Mostrar os detalhes de um produto. Para isso, quando o usuário digitar o ID do 
#     produto escolhido, você deve encontrar o item e exibir apenas o item selecionado por ele.
#   - Deletar um item da lista de produtos. Dado um ID de um produto fornecido pelo usuário 
#     você deve apagar o item da lista de produtos.
#   - Usando o código completo com todos os requisitos implementados corretamente, chegou a hora 
#     de melhorar o seu código, você deve:
#   - Encontrar pontos de melhorias no código se achar necessário, explicar as mudanças e também 
#     o porquê de terem alterado o código. Você adicionará um comentário para explicar o que a função 
#     faz e como ela faz e o que sua mudança provoca de melhoria em comparação com o código original.
#   - Todas as funções DEVEM ser funcionais. Você pode adicionar fluxos de condição , tratativas de erro 
#     e também mensagens informativas para possíveis comportamentos inesperados do cliente
#   - Ex.: Usuário precisa digitar um valor X mas ele acaba digitando Y. Então você deve auxiliar o usuário 
#     onde ele cometeu esse erro e o que ele precisa fazer para corrigir.
#   - Ex2.: O usuário digitou um ID de um produto que não existe, como o programa deveria se comportar?


import time

# criando uma lista para armazenar os dados que serão cadastrados pelo usuário
# dentro da lista será criado um dicionário para armazenar os atributos de cada produto
lista_produtos = [
    {'id': 1, 'nome': 'Brigadeiro', 'preço': 4.0}, 
    {'id': 2, 'nome': 'Torta de Limão', 'preço': 13.0}, 
    {'id': 3, 'nome': 'Brigadeiro de Maracujá', 'preço': 4.50}, 
    {'id': 4, 'nome': 'Cocada', 'preço': 3.0}
    ]

id_produto = 1


# definindo a função para criar o menu
def menu():

    while True:

        # adiconando as opções do menu que serão apresentadas ao usuário, utilizamos a função print()
        print("\n ** Loja de Doces da May **\n" + "\n * MENU * \n")
        print("1 - Adicionar")
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")

        # criando variável para que o usuário escolha a opção desejada
        opcao = input("\nEscolha a opção desejada:\n")

        # definindo as ações para cada opção do menu
        # "ao digitar a opção x, o programa deve fazer y"
        if opcao == "1": # input retorna str, por isso é necessário colocar as aspas no valor ou convertê-lo para realizar a comparação
            adicionar_produto() # chamando a função que vai executar a ação
        elif opcao == "2":
            print("exibir detalhes")
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            print("opcao apagar doce")
        elif opcao == "5":
            listar_todos()
        elif opcao == "0":
            break
        # adicionando opção para tratar erros de digitação pelo usuário
        else: # else não tem comparação, se o usuário escolher uma opção que não existe no sistema ele será executado
            print("Opção inválida, por favor escolha uma opção do menu")
        # é necessário dar novamente a opção de escolha ao usuário, para isso usamos laço de repetição no início da função


# é recomendado criar uma função para cada ação a ser desempenhada pelo programa
# isso facilita a manutenção do código e controle de erros


# criando a função que vai gerar o id do produto
def gerar_id_produto():
    
    # criando condição para verificar se a lista começa em 0
    if len(lista_produtos) == 0:
        return 1
    
    # criando função que pega a posição do último item da lista e soma 1 para gerar o id
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_produtos[0].get("id") + 1
    return novo_id


# definindo a função para o usuário adicionar um produto
def adicionar_produto():

    # criando as variáveis e solicitando as informações
    # exceto o código de identificação do produto que não pode se repetir e deve ser gerado pelo sistema
    nome_produto = input("\nDigite o nome do produto:\n")
    preco_produto = input("\nDigite o preço do produto:\n")
    
    # criando dicionário para armazenar os atributos dos produtos (definindo um dado)
    produto = {
        "id": gerar_id_produto(), # chamando a função que gera o identificador único
        "nome": nome_produto,
        "preço": float(preco_produto), # necessário converter para número para realizar cálculos futuros
    }

    # adicionando produtos cadastrados na lista de produtos
    lista_produtos.append(produto)

    # informando ao usuário que o produto foi adicionado e exibindo os seus atributos
    print(f"\nO produto foi adicionado com sucesso!\n{produto}")


# criando a função para atualizar um produto já cadastrado
def atualizar_produto():
    id_produto = input("Digite o ID do produto para atualizar:\n")

    # criando laço para percorrer a lista até encontrar o produto solicitado pelo usuário
    for index in range(len(lista_produtos)):

        # crinado condição para "atualizar o id encontrado
        if lista_produtos[index].get("id") == int(id_produto):
            novo_valor = input("Digite o novo valor do produto:\n")
            lista_produtos[index]["preço"] = float(novo_valor)

            # informando ao usuário que o produto foi atualizado e exibindo os seus atributos
            print(f"\nO produto foi atualizado com sucesso!\n{lista_produtos[index]}")


# criando a função para exibir uma lista com todos osprodutos cadastrados no sistema
def listar_todos():
    for index in range(len(lista_produtos)): # laço que percorre a lista

        # exibindo a lista para o usuário
        print(f"{lista_produtos[index]}\n") 


#chamando a função principal para que o programa seja executado e visualizado pelo usuário
menu()
