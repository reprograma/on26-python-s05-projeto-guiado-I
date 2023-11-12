##CRUD - CREATE, READ, UPDATE DELETE


# Quero opção de:
# Criar doce
# Exibir detalhes de um doce
# Atualizar doce
# Apagar doce
# Exibir lista de todos os doces

listaProdutos = [
    
]
carrinho = {}
numero_pedido = 0

def menuInicial():
    while True:
        print("\n MENU INICIAL \n")
        print("1 - Sou cliente")
        print("2 - Sou funcionário")
        print("0 - Sair")

        opcao = input("Digite a opção escolhida (atráves do número): \n")
        if opcao == "1":
            menuCliente()
        elif opcao == "2":
            menu()
        elif opcao == "0":
            break
        else:
            print("Escolha uma opção válida")


def menuCliente():
    while True:
        print("\n MENU DO CLIENTE \n")
        print("1 - Exibir todos os produtos")
        print("2 - Exibir detalhes")
        print("3 - Adicionar produto ao carrinho")
        print("4 - Remover produto do carrinho")
        print("5 - Total do carrinho")
        print("6 - Finalizar compra")
        print("0 - Sair")

        opcao = input("Digite a opção escolhida (atráves do número): \n")
        if opcao == "1":
            listarTodos()
        elif opcao == "2":
            exibirDetalhes()
        elif opcao == "3":
            adicionarAoCarrinho()
        elif opcao == "4":
            removerDoCarrinho()
        elif opcao == "5":
            calcularTotalCarrinho()
        elif opcao == "6":
            finalizarCompra()
        elif opcao == "0":
            menuInicial()
        else:
            print("Escolha uma opção válida.")





def menu():
    while True:
        print("\n ** MENU LOJA REPROGRAMA **\n")
        print("1 - Adicionar")
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")

        opcao = input("Escola a opção dejesada:\n")
        
        if opcao == "1":
            adicionarProduto()
        elif opcao == "2":
            exibirDetalhes()
        elif opcao == "3":
            atualizarProduto()
        elif opcao == "4":
            removerProduto(id)
        elif opcao == "5":
            listarTodos()
        elif opcao == "0":
            break
        else:
            print("Escolha uma opção válida. EXEMPLO: se quer a opção 'Exibir todos', digite 5.")
            


def adicionarAoCarrinho():
    idProduto = input("Digite o ID do produto que deseja adicionar ao carrinho:\n")
    quantidade = input("Digite a quantidade desejada:\n")
    
    try:
        idProduto = int(idProduto)
        quantidade = int(quantidade)
    except ValueError:
        print("ID do produto e quantidade devem ser números inteiros.")
        return
    
    for produto in listaProdutos:
        if produto["id"] == idProduto:
            if idProduto in carrinho:
                carrinho[idProduto] += quantidade
            else:
                carrinho[idProduto] = quantidade
            print(f"{quantidade} {produto['nome']} adicionado(s) ao carrinho.")
            return
    print(f"Produto com ID {idProduto} não encontrado na lista de produtos.")

def removerDoCarrinho():
    idProduto = input("Digite o ID do produto que deseja remover do carrinho:\n")
    try:
        idProduto = int(idProduto)
    except ValueError:
        print("ID do produto deve ser um número inteiro.")
        return
    
    if idProduto in carrinho:
        quantidade = carrinho[idProduto]
        del carrinho[idProduto]
        print(f"{quantidade} item(s) removido(s) do carrinho.")
    else:
        print(f"Produto com ID {idProduto} não encontrado no carrinho.")

def calcularTotalCarrinho():
    total = 0
    for idProduto, quantidade in carrinho.items():
        for produto in listaProdutos:
            if produto["id"] == idProduto:
                total += quantidade * produto["preço"]
    return total

def finalizarCompra():
    global numero_pedido
    if not carrinho:
        print("Seu carrinho está vazio. Adicione produtos antes de finalizar a compra.")
        return
    
    numero_pedido += 1
    total = calcularTotalCarrinho()
    
    print("\nResumo da Compra:")
    print("Número do Pedido:", numero_pedido)
    print("Itens no Carrinho:")
    for idProduto, quantidade in carrinho.items():
        for produto in listaProdutos:
            if produto["id"] == idProduto:
                print(f"{produto['nome']} x{quantidade} - R${produto['preço']:.2f} cada")
    print("Total da Compra: R${:.2f}".format(total))
    
    carrinho.clear()
    print("Compra finalizada. Obrigado!")

#Adiciona produtos à lista
def adicionarProduto():
    nomeProduto = input("Digite o nome do produto:\n")
    preçoProduto = (input("Digite o preço do produto:\n"))
    produto = {
        "id": gerarIdProduto(),
        "nome": nomeProduto,
        "preço": float(preçoProduto)
    }
    listaProdutos.append(produto)

    print(listaProdutos)

##Função de remover o doce da lista
def removerProduto(id):
    for produto in listaProdutos:
        if produto["id"] == id:
            listaProdutos.remove(produto)
            print(f"Doce com ID {id} removido.")
            return
    print(f"Não foi possível encontrar doce com ID {id}")


##Função de exibir detalhes sobre um produto de escolha
def exibirDetalhes():
    idProduto = input("Digite o ID do produto para exibir os detalhes:\n")
    for produto in listaProdutos:
        if produto["id"] == int(idProduto):
            print("\nDetalhes do Produto:")
            print(f"ID: {produto['id']}")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R${produto['preço']:.2f}")
            return
    print(f"Não foi possível encontrar um produto com ID {idProduto}")


#Essa cria um id para o produto. Primeiro ela vê se a lista está vazia. Se sim, então o ID do produto novo é 
#o númeroo 1, se não, é o número do id anterior mais 1.
def gerarIdProduto():
    if len(listaProdutos) == 0:
        return 1
    listaProdutos.sort(key=id, reverse=True)
    novoID = listaProdutos[0].get("id") +1
    
    return novoID


#Essa atualiza valores dos produtos como id, nome, preço.
def atualizarProduto():
    idProduto = input("Digite o ID do produto para atualizar:\n")
    for index in range(len(listaProdutos)):
        if listaProdutos[index].get("id") == int(idProduto):
           novoValor =  print("Digite o novo valor do produto")
           listaProdutos[index]["preço"] = float(novoValor)
           print(f"O produto foi atualizado com sucesso! {listaProdutos[index]} ")


##A função "listarTodos()" lista todos os produtos que foram adicionados à loja. 
# Ela verifica se a lista está vazia. Se não, ela imprime os produtos em uma tabela. 
# Se sim, mostra uma mensagem dizendo que a lista está vazia.
def listarTodos():
    print("\nLista de Produtos:")
    print("{:<5} {:<20} {:<10}".format("ID", "Nome", "Preço"))
    
    if len(listaProdutos) > 0:
        for produto in listaProdutos:
            print("{:<5} {:<20} R${:<10.2f}".format(produto["id"], produto["nome"], produto["preço"]))
    else:
        print("A lista de produtos está vazia.")


menuInicial()
    

