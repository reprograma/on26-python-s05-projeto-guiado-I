# Projeto 1 - Reprograma Python 
# Como Desafio para casa você precisará utilizar o código feito na aula e implementar as seguintes funcionalidades restantes:
# 1- Mostrar os detalhes de um produto. Para isso, quando o usuário digitar o ID do produto escolhido, você deve encontrar o item e exibir apenas o item selecionado por ele.
# 2- Deletar um item da lista de produtos. Dado um ID de um produto fornecido pelo usuário você deve apagar o item da lista de produtos.
# Agora, usando o código completo com todos os requisitos implementados corretamente, chegou a hora de melhorar o seu código, você deve:
# 1- Encontrar pontos de melhorias no código se achar necessário, explicar as mudanças e também o porquê de terem alterado o código. Você adicionará um comentário para explicar o que a função faz e como ela faz e o que sua mudança provoca de melhoria em comparação com o código original
# 2- Todas as funções DEVEM ser funcionais. Você pode adicionar fluxos de condição , tratativas de erro e também mensagens informativas para possíveis comportamentos inesperados do cliente
# Ex.: Usuário precisa digitar um valor X mas ele acaba digitando Y. Então você deve auxiliar o usuário onde ele cometeu esse erro e o que ele precisa fazer para corrigir.
# Ex2.: O usuário digitou um ID de um produto que não existe, como o programa deveria se comportar?
# Importante: Você tem a liberdade de fazer qualquer alteração no código que ache pertinente, mas lembre-se de sempre justificar.

lista_produtos = [] #Esvaziei a lista para despoluir o código

def menu():
    while True:
        print("\n ** MENU LOJA REPROGRAMA **\n")
        print("1 - Adicionar")
        print("2 - Consultar produto para exibir detalhes")
        print("3 - Atualizar o preço de um produto")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")
        opcao = int(input("Escolha a opção desejada\n"))

        match opcao: #Alterei para match e case ao invés dos ifs porque assim o código será executado de forma mais rápida
          case 1:
            adicionar_produto()
          case 2:
            exibir_detalhes()
          case 3:
            atualizar_produto()
          case 4:
              apagar_produto()
          case 5:
              listar_todos()
          case 0:
              break
          case _:
              print("Opção inválida, por favor escolha uma opção do menu\n")

def exibir_detalhes(): # Criando a função para exibir detalhes sobre certo ID provido pelo user
    consulta_detalhes = int(input("\nDigite a ID do produto que deseja consultar: "))

    produto_encontrado = False  # Variável para rastrear se o produto foi encontrado

    for produto in lista_produtos:
        if consulta_detalhes == produto.get("id"): #Se a id encontrada for igual ao input do user
            print(f"\nO produto consultado é {produto}\n")
            produto_encontrado = True
            break  # Para sair do loop assim que o produto for encontrado
    if not produto_encontrado: # Aqui vamos lidar com o usuário caso o produto não seja encontrado
        print("Produto não encontrado. Tente novamente!")

def apagar_produto(): # Criando função para apagar certo produto da lista
  id_produto = int(input("\nDigite a ID do produto que deseja remover:\n"))

  for produto in lista_produtos:
          if produto["id"] == id_produto:
              lista_produtos.remove(produto)
              print(f"Produto com ID {id_produto} removido com sucesso.")
              return
          if not lista_produtos:
            print(f"Produto com ID {id_produto} não encontrado na lista.")
  menu()

def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_produtos[0].get("id") + 1

    return novo_id
            
def adicionar_produto():
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = input("Digite o preço do produto (no formato de 0.00):\n")

    produto = {
        "id": gerar_id_produto(),
        "nome": nome_produto,
        "preço": float(preco_produto),
    }
    lista_produtos.append(produto)

    print(lista_produtos)

def atualizar_produto():
    id_produto = int(input("Digite a ID do produto para atualizar:\n")) 

    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("id") == int(id_produto):
            novo_valor = input("Digite o novo valor do produto:\n")
            lista_produtos[index]["preço"] = float(novo_valor)
            print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")
        if not id_produto: #Lidando com o user que digitou um valor inexistente
            print("Produto não encontrado. Tente novamente!") 

def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")

menu()
