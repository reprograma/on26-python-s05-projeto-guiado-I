# quero opção de:
# adicionar doce
# exibir detalhe de um doce
# atualizar doce
# apagar doce
# exibir a lista de todos os doces

lista_produtos = []


def menu():
    while True :
        print('\n ** MENU LOJA REPROGRAMA **\n')
        print('1 - adicionar')
        print('2 - exibir detalhes')
        print('3 - atualizar')
        print('4 - apagar')
        print('5 - exibir todos')
        print('0 - sair')

        opcao = input('escolha a opção desejada\n')

        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            print('opção exibir detalhes doce')
        elif opcao == '3':
            atualizar_produto()
        elif opcao == '4':
            print('opção apagar doce')
        elif opcao == '5':
            listar_todos()    
        elif opcao == '0':
            break
        else:
            print('opção inválida, por favor escolha uma opção do menu')    


def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=lambda produto: produto.get('id'), reverse=True)
    novo_id = lista_produtos[0].get('id') + 1

    return novo_id


def adicionar_produto():
    nome_produto = input('digite o nome do produto:\n')
    preco_produto = input('digite o preço do produto:\n')

    produto = {'id':gerar_id_produto(), 'nome': nome_produto, 'preço': float(preco_produto)}

    lista_produtos.append(produto)

    #print(f'isso é o valor do produto inteiro {lista_produtos[0]}')

    #print(f'isso é o valor do ID do produto escolhido {lista_produtos[0].get('nome')}')

    print(lista_produtos)


def atualizar_produto():
    id_produto = input('digite o ID do produto para atualizar:\n')

    for index in range(len(lista_produtos)):
        if lista_produtos[index].get('id') == int(id_produto):
            novo_valor = input('digite o novo valor do produto:\n')
            lista_produtos[index]['preço'] = float(novo_valor)
            print(f'o produto foi atualizado com suceso! {lista_produtos[index]}')

            #print('produto_encontrado')


def listar_todos():
    for index in range(len(lista_produtos)):
     print(f'{lista_produtos[index]}\n')


def exibir_detalhes():
    id_doce = input('forneça o ID do produto:\n')
    for produto in lista_produtos:
        if produto.get('id') == int(id_doce):
            print(produto)
            break


def deletar():
    id_produto = input('digite o ID do produto para deletar:\n')

    for produto in lista_produtos:
        if produto.get('id') == int(id_produto):
            lista_produtos.remove(produto)
            break


menu()
