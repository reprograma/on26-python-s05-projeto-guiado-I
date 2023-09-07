# Quero opção de:
# Adicionar doce
# Exibir detalhe de um doce
# Atualizar doce
# Apagar doces
# Exibir a lista de todos os doces


# O módulo time aqui não está sendo usado em nenhuma parte
# Excluiria (deixei para a prof. ver)
import time

# Inicia a lista de produtos vazia e o contador de IDs
lista_produtos = []
id_produto = 1

#Função para exibir o menu
def menu():
    while True:
        # Atribui um nome a loja para me lembrar da cliente e o que ela quer
        # Não mudei nada no print, acredito que ele tá bem claro
        print("\n ** MENU MAYHARRA'S CANDY CO **\n")
        print("1 - Adicionar")
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")

        # A palavra "opcao_menu" deixa mais claro que é uma escolha no menu, atualizei
        opcao_menu = input("Escolha a opção desejada\n")

        if opcao_menu == "1":
            adicionar_produto()
        elif opcao_menu == "2":
            detalhar_produto()
        elif opcao_menu == "3":
            atualizar_produto()
        elif opcao_menu == "4":
            cancelar_produto()
        elif opcao_menu == "5":
            listar_todos()
        elif opcao_menu == "0":
            break
        else:
            print("Opção inválida, por favor tente novamente")
# Alterei a redação para o usuário continuar tentando.

# Sinceramente não teria uma sugestão melhor porque apesar de saber explicar eu não saberia fazer sozinha
# É uma função para criar um novo número de identificação automaticamente
# No if ela olha para a lista e se ela estiver vazia ela cria o ID inicial em 1
# Se a lista não estiver vazia, a função sort ordena a lista de cada produto, mas em ordem reversa
# Significa que pega o maior ID da lista e adiciona 1 a ele
# Esse novo id é o que a função retorna garantindo que cada produto tem um ID único
def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_produtos[0].get("id") + 1

    return novo_id

# Não mudei porque faz todo sentido pra mim
# A função literalmente adiciona um produto na lista com as infos que o usuário informar
def adicionar_produto():
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = input("Digite o preço do produto:\n")

# Aqui cada produto está dentro de um dicionário que é alimentado pelo usuário
# Como se a função colocasse ele na loja, que é uma lista
# Significa que o doce agora faz parte do menu
# Por fim a função mostra a lista de todos os doces da loja
# Não sei como faria um dicionário diferente
    produto = {
        "id": gerar_id_produto(),
        "nome": nome_produto,
        "preço": float(preco_produto),
    }
    lista_produtos.append(produto)

    print(lista_produtos)

# Função criada para exibir os detalhes com base no ID
# O usuário precisa digitar o ID do produto para exibir os detalhes
def detalhar_produto():
    id_produto = int(input("Digite o ID do produto para exibir os detalhes:\n"))

# "produto" aqui, e na função deletar, é uma variável que acessa os campos do dicionário dentro da lista
# Para cada produto dentro da lista:
#   Se o id do produto digitado for encontrado, imprimi os detalhes
#   Retorna e encerra
#   Se o id não for encontrado, aparece mensagem de erro ao usuário
    for produto in lista_produtos:
        if produto["id"] == id_produto:
            print(f"Detalhes do Produto - ID: {produto['id']}, Nome: {produto['nome']}, Preço: R${produto['preço']: .2f}")
        return
    print("Produto não encontrado.")

# Função criada para deletar um produto da lista baseado no ID
# O usuário precisa digitar o ID do produto a ser cancelado
def cancelar_produto():
    id_produto = int(input("Digite o ID do produto que deseja apagar:\n"))

# Para cada produto dentro da lista:
#   Se o id do produto digitado for encontrado, o método "remove" apaga o produto da lista
#       E o usuário recebe a mensagem de sucesso na operação
#       retorna e finaliza 
#   Se não encontrar o id aparece mensagem de erro ao usuário

    for produto in lista_produtos:
        if produto["id"] == id_produto:
            lista_produtos.remove(produto)
            print("Produto apagado com sucesso!")
        return
    print("ID do produto não encontrado, por favor tente novamente.")

# Fiquei pensando e se o usuário quiser altualizar o nome do produto também?
# Alterei a função para a variável produto, não sei usar pelo INDEX
# A função agora atualiza um produto (seu nome ou preço) com base no ID
# Começa pedindo para o usuário digitar o ID que será atualizado
def atualizar_produto():
    id_produto = int(input("Digite o ID do produto para atualizar:\n"))

# Aqui a função verifica cada produto da lista para ver se o ID do produto foi o ID digitado pelo usuário
# Se o produto for encontrado, mostramos os detalhes para o usuário ter certeza antes de modificar
    for produto in lista_produtos:
        if produto["id"] == id_produto:
            print(f"Produto encontrado: ID: {produto['id']}, Nome: {produto['nome']}, Preço: R${produto['preço']:.2f}")
            
            # Aqui perguntamos o que o usuário quer atualizar
            # Ele vai escolher pelo letra inicial, achei o "upper" na documentação que converte a str em letra maiúscula para usar no if
            escolha = input("O que você deseja atualizar? (N para nome, P para preço, qualquer outra tecla para cancelar)\n").upper()
            
            # Se o usuário escolher o "N" ele vai pedir pro usuário digitar o novo nome
            # Depois mostra a mensagem de que foi atualizado
            # Se o usuário escolher o "P" ele pede para digitar o novo valor do produto
            # O código vai tentar converter esse valor em um float
            # Se der certo, atualizo o preço
            # Se usuário digitar algo que não seja um número válido, mostra msg de erro
            # Se o usuário escolher cancelar, mostra a msg de cancelamento
            # Depois de atualizar ou cancelar retorna e fecha
            if escolha == "N":
                novo_nome = input("Digite o novo nome do produto:\n")
                produto["nome"] = novo_nome
                print("Nome do produto atualizado com sucesso!")
            elif escolha == "P":
                novo_valor = input("Digite o novo valor do produto:\n")
                try:
                    novo_valor = float(novo_valor)
                    produto["preço"] = novo_valor
                    print("Preço do produto atualizado com sucesso!")
                except ValueError:
                    print("Por favor, insira um valor válido.")
            else:
                print("Operação cancelada.")
            return
    # Se nenhum ID for encontrado aparece a msg de erro
    print("ID do produto não encontrado, por favor tente novamente.")

# Não mudaria nada, não sei fazer o INDEX apesar de entender
# A função lista todos os produtos da doceria
# Ela percorre todos os produtos da lista e imprime cada um deles
# Eles são mostrados em uma linha separada
def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")

# função que inicia a execução do programa
menu()