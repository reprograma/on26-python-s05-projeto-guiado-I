# Inclui o UUID para gerar o id por motivo de organização e segurança, 
# usei a versão 4 que usa números aleatórios ou pseudo-aleatórios.
# Teste viu, não sei nem se podia, estava pesquisando e achei uma boa ideia. 
import uuid

lista_produtos = []

def menu():
    while True:
        print("\n ** MENU LOJA REPROGRAMA **\n")
        print("1 - Adicionar")
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")

        opcao =  input("Escolha a opção desejada:\n")
        if opcao == "1":
            adicionar_produto()    
        elif opcao == "2":
            exibir_detalhes_produto()   
        elif opcao == "3":
            atualizar_produto()        
        elif opcao == "4":
            apagar_produto()        
        elif opcao == "5":
            listar_todos()       
        elif opcao == "0":
            break
        else:
            print("Opção inválida, por favor escolha uma opção do menu")

# Inclui uma variável utilizando o uuid para gerar o identificador de cada produto.
# Pensei em colocar o insert ou extend ao invés do append porque ele me dá a 
# condição de adicionar um item no id desejado e o outro mescla duas listas e transforma em uma, 
# mas desisti por que achei que não faria sentido.
def adicionar_produto():
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = float(input("Digite o preço do produto:\n"))
    id_produto = str(uuid.uuid4())
    produto ={"id": id_produto, "nome": nome_produto,"preço": preco_produto}
    lista_produtos.append(produto)
    print(f"Produto '{nome_produto}' adicionado com sucesso!")

def exibir_detalhes_produto():
    id_produto = input("Digite o ID do produto que deseja visualizar: ")
    for produto in lista_produtos:
        if produto["id"] == id_produto:
            print(f"Detalhes do Produto: \n")
            print(f"ID: {produto['id']} \n")
            print(f"Nome: {produto['nome']}\n")
            print(f"Preço: R${produto['preco']:.2f}\n")
            return
    print("Produto não encontrado.\n")

# Mudei a função só por que teve uma hora que não consegui mais entender, hehe. Me desculpe!
def atualizar_produto():
    id_produto = input("Digite o ID do produto que deseja atualizar: \n")
    for produto in lista_produtos:
        if produto["id"] == id_produto:
            novo_preco = float(input("Digite o novo preço do produto: \n"))
            produto["preco"] = novo_preco
            print("Preço do produto atualizado com sucesso.\n")
            return
    print("Produto não encontrado.\n")

def apagar_produto():
    id_produto = input("Digite o ID do produto que deseja apagar: \n" )
    for produto in lista_produtos:
        if produto["id"] == id_produto:
            lista_produtos.remove(produto)
            print("Produto apagado com sucesso.\n")
            return
    print("Produto não encontrado.\n")

def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")

menu()