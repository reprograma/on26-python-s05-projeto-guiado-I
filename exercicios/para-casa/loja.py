'''
Este é um programa para uma loja de doces com as seguintes funcionalidades:
- Adicionar novos doces ao menu
- Exibir detalhes de um doce
- Atualizar doces
- Apagar doces
- Exibir a lista de todos os doces

Gostaria de mostrar o preço com formato R$00,00, mas não consegui. 
Também não soube exibir o produto inserido na opção 1 na formatação bonitinha como fiz nas outras funções. :(
'''
#Declara uma lista de produtos vazia.
lista_produtos = []

#Função principal. Mostra o menu de opções para o usuário e recebe uma escolha de ação.
def menu():
#O while é usado para mostrar o menu principal depois que cada ação é realizada, até o que o usuário decida sair do programa.
    while True:
        print("\n ** MENU LOJA REPROGRAMA ** \n")
        print("1 - Adicionar produto")
        print("2 - Exibir detalhes de um produto específico")
        print("3 - Atualizar preço de um produto")
        print("4 - Apagar um produto")
        print("5 - Exibir todos os produtos disponíveis")
        print("0 - Sair do programa \n")

        opcao = input("Escolha a opção desejada\n")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            exibir_produto()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            apagar_produto()
        elif opcao == "5":
            listar_todos()
        elif opcao == "0":
            print("Sair")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção do menu.")

#Função de adicionar produto
def adicionar_produto():
#try verifica se o input do usuário é válido. Se o usuário inserir uma string em preço, por exemplo, o programa mostra a mensagem de erro.
    try:
        nome_produto = input("Digite o nome do produto:\n")
        preco_produto = float(input("Digite o preço do produto:\n"))
#valida se o preço inserido é positivo
        if preco_produto > 0:
#cria um dicionário de produtos que armazena 3 conjuntos de chave: valor que caracterizam o doce a ser cadastrado
            produto = {
                "id": gerar_id_produto(),
                "nome": nome_produto,
                "preço": preco_produto
            }
#adiciona o novo produto inserido à lista de dicionários definida fora da função.
            lista_produtos.append(produto)
#ordena a lista pelo valor do id
            lista_produtos.sort(key=id)
        else:
            print("Preço deve ser um valor positivo!")
    except(ValueError):
        print("Preço deve ser um valor numérico!")

#Função de gerar ID de um novo produto cadastrado na função de adicionar produto
def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
#ordena produtos pelo id em ordem decrescente para que o primeiro item tenha o maior id. Assim, sabe-se qual deve ser o próximo id.
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_produtos[0].get("id") + 1
    return novo_id

#Função de exibir um produto específico
def exibir_produto():
    try:
        id_produto = int(input("Digite o ID do produto que você deseja visualizar:\n"))
#testa se o id inserido está na lista de ids disponíveis. Roda entre todos os ids para encontrar o id desejado e exibe as informações.
        if id_produto <= len(lista_produtos) and id_produto >0:
            for doce in lista_produtos:
                if doce["id"] == id_produto:
#imprime as informações em formato mais visual para o usuário.
                    print(f"\nAs informações do produto de ID {id_produto} são:\n")
                    for chave, valor in doce.items():
                        print(f"{chave}: {valor}")
        else:
            print("ID inválido!")

    except(ValueError):
        print("O ID do produto deve ser um valor inteiro!")

#Função de atualizar preço de um produto específico
def atualizar_produto():
        try:
            id_produto = int(input("Digite o ID do produto a ser atualizado:\n"))
            novo_valor = float(input("Digite o novo valor do produto:\n"))
            if id_produto <= len(lista_produtos) and id_produto >0:
                for doce in lista_produtos:
                    if doce["id"] == id_produto:
                        doce["preço"] = novo_valor
                        print(f"\nAs informações atualizadas do produto de ID {id_produto} são:\n")
                        for chave, valor in doce.items():
                            print(f"{chave}: {valor}")
            else:
                print("ID inválido!")
        except(ValueError):
            print("O ID do produto deve ser um valor inteiro!")

#Função de apagar um produto específico
def apagar_produto():
    try:
        id_produto = int(input("Digite o ID do produto a ser apagado:\n"))
        if id_produto <= len(lista_produtos) and id_produto > 0:
            for index in range(len(lista_produtos)):
                if lista_produtos[index].get("id") == id_produto:
                    lista_produtos.pop(index)
                    print(f"O produto {id_produto} foi removido com sucesso!")
        else:
            print("ID inválido!")
    except(ValueError):
        print("O ID do produto deve ser um valor inteiro")

#Função de listar as informações de todos os produtos disponíveis
def listar_todos():
    if not lista_produtos:
        print("Nenhum doce foi registrado ainda. Favor utilizar a opção 1 para adicionar doces.")
    else:
        for doce in lista_produtos:
            print("\nInformações de", doce["nome"], ":")
            for chave, valor in doce.items():
                print(f"{chave}: {valor}")

#Inicia o programa
menu()