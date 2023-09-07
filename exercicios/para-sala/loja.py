# Quero opção de:
# Adicionar doce
# Exibir detalhes de um doce
# Atualizar doce
# Apagar doces
# Exibir a lista de todos os doces

lista_produtos = [
    {'id': 2, 'nome': 'novo produto2 ', 'preço': 3.0},
    {'id': 3, 'nome': 'novo produto3 ', 'preço': 4.0},
    {'id': 1, 'nome': 'novo produto1 ', 'preço': 3.0},
]

def menu():
    while True:
        print('\n ** MENU LOJA REPROGRAMA **\n')
        print('1 - Adicionar')
        print('2 - Exibir Detalhes')
        print('3 - Atualizar')
        print('4 - Apagar')
        print('5 - Exibir Todos')
        print('0 - Sair')
          
        opcao = input('Escolha a opção desejada\n')
    
        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            print('Opção exibir detalhes doce')
        elif opcao == '3':
            atualizar_produto()
        elif opcao == '4':
            print('Opção apagar doce')
        elif opcao == '5':
            print('Opção exibir todos os doces')
        elif opcao == '0':
            print('Sair')
            break
        else:
          print('Opção inválida, por favor escolha uma opção do menu')

#dicionário dict
def adicionar_produto():
    nome_produto = input('Digite o nome do produto:\n')
    preco_produto = input('Digite o preço do produto:\n')

    produto = {
        'id': gerar_id_produto(), 
        'nome': nome_produto, 
        'preço': float(preco_produto),
    }

    lista_produtos.append(produto)

    print(lista_produtos)

def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=id, reverse=True)

    novo_id = lista_produtos[0].get('id') + 1

    return novo_id

def atualizar_produto():
    id_produto = input('Digite o ID do produto para atualizar:\n')

    for index in range (len(lista_produtos)):
        if lista_produtos[index].get('') == int(id_produto):
            novo_valor = input('Digite o novo valor do produto:\n')
            lista_produtos[index]['preço'] = novo_valor
            print(f'O produto foi atualizado com sucesso! {lista_produtos[index]}')

def listar_todos():
    for index in range(len(lista_produtos)):
        print(f'{lista_produtos[index]}\n')

menu()