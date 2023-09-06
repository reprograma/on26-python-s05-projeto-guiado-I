lista_doces=[{'Nome': 'Mousse de Cupuaçu', 'Preço': 5.0 , 'id': 0}, {'Nome': 'Sorverte de Tucumã', 'Preço': 8.0 , 'id': 1}, {'Nome': 'Bala de castanha', 'Preço': 9.0 , 'id': 2}]

def menu():
    
    while True:
        print('** MENU LOJA DE DOCES **')
        print('1 - Todos os doces')
        print('2 - Buscar doce')
# Excluí alguns itens para que eu pudesse vizualizar melhor os itens solicitados.
            
        opcao= input('Digite a opção desejada: \n')

        if opcao =='1':
            print(lista_doces)
        
        elif opcao =='2':
            print('Localize um doce através de ID')
            break

        else:
            print('Opção inválida! Digite as opções listadas\n')
# A ideia era que inicialmente o cliente tivesse apenas essas duas opções para poder prosseguir de acordo com a opção escolhida.

def gerar_id_doces():
    if len(lista_doces) == 0:
        return 1
    lista_doces.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_doces[0].get("id") + 1
    return novo_id
# No debug as variáveis são apontadas seguindo a orientação da lista de doces.

#Adicionando função para remover

def remover_doce():
    novo_id = int(input('Remover do carrinho\n'))
    for c in lista_doces:
        if c.get('id')==int(novo_id):
            lista_doces.remove(c)
            print('Doce removido com sucesso')
            return



            

menu()