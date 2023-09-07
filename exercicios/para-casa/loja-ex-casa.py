# Quero opção de:
# Adicionar doce
# Exibir detalhe de um doce
# Atualizar doce
# Apagar doces
# Exibir a lista de todos os doces
import time

# Mudei o nome dos doces para os doces que eu mais gosto e que são mais comuns.
lista_produtos = [{'id': 1, 'nome': 'Pudim', 'preço': 7.0}, {'id': 2, 'nome': 'Brigadeiro', 'preço': 2.0}, {'id': 3, 'nome': 'Brownie', 'preço': 10.0}]

id_produto = 1

def menu():
    while True:
        print("\n ** MENU LOJA REPROGRAMA **\n")
        print("1 - Adicionar")
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")

        opcao = input("Escolha a opção desejada:\n")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            print("opcao exibir detalhes doce")
        elif opcao == "3":
             atualizar_produto() #retirei a lista de produtos porque estava dando erro no código
            #atualizar_produto([lista_produtos])
        elif opcao == "4":
            apagar_produto()
        elif opcao == "5":
            listar_todos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida, por favor escolha uma opção do menu")

#Retirei o key e coloquei o type como foi orientado, porém dá erro quando tento incluir mais doces não roda. Então preferi manter assim.
def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key= lambda produto:produto.get("id"), reverse=True)
    novo_id = lista_produtos[0].get("id") + 1
    return novo_id

# aqui foi adicionada uma função para caso o usuário ponha um número no lugar de nome apareça uma mensagem de erro 
# # realizado em grupo de estudos
    def adicionar_produto():
        nome_produto = input("Digite o nome do produto:\n")
        while any(char.isdigit() for char in nome_produto):
            print("O nome do produto não pode conter números. Por favor, insira um novo nome.")
            nome_produto = input("Digite o nome do produto:\n")
        preco_produto = float(input("Digite o preço do produto:\n"))
        produto = {
            "id": gerar_id_produto(),
            "nome": nome_produto,
            "preço": float(preco_produto),
        }
        lista_produtos.append(produto)
        
# foi necessário incluir try e except, pois quando eu testava com string estava dando erro
def atualizar_produto():
        try:
            id_produto = int(input('Digite o ID do produto para atualizar:\n'))
            for produto in lista_produtos:
                if produto.get('id') == id_produto:
                    novo_id = input('Digite o novo nome do produto:\n')
                    novo_preco = float(input('Digite o novo preço do produto:\n'))
                    produto['nome'] = novo_id
                    produto['preço'] = novo_preco
                    print ('Produto atualizado com sucesso!\n')
                    print (f'(Lista atualizada:\n {lista_produtos})')
                    return 
            print ('Produto não encontrado. Digite um ID de produto válido')
        except Exception:
            print ('Voçê precisa inserir um número de ID de produto válido.')
    
def listar_todos():
    for index in range(len(lista_produtos)):
        print(f'{lista_produtos[index]}\n')

# No print eu quis já deixar mostrando a lista com a alteração.
def apagar_produto():
    try:
        id_produto= int(input("Informe o ID do produto que deseja excluir:\n"))
        for produto in lista_produtos:
            if produto.get('id')==int(id_produto):
                lista_produtos.remove(produto)
                print('Produto deletado com sucesso!')
                print(f'Lista atualizada:{lista_produtos}')
                return
        print('Produto não encontrado, digite um ID de produto válido.')
    except Exception:
        print('Voçê precisa inserir um número de ID de produto válido.')



menu()