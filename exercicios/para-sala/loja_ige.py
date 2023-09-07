#quero opção de:
#criar doces
#detalhar doces
#atualizar
#deletar doces
#listar todos os doces
import time

lista_menu = [{'id': 3, 'nome': 'asdasdas', 'preço': 32.0}, {'id': 2, 'nome': 'asd', 'preço': 2.0}, {'id': 1, 'nome': 'a', 'preço': 1.0}, {'id': 4, 'nome': '23123', 'preço': 13123.0}]

id_produto = 1
def menu():
    while True:
        print("\n ** Menu Loja Reprograma **\n")
        print('0 - Sair')
        print('1 - Adicionar')
        print('2 - Exibir detalhes')
        print('3 - Atualizar')
        print('4 - Apagar')
        print('5 - Exibir todos')
    
        opcao = input('Informe a opção desejada: \n')
    
        if opcao == '0':
            break
        elif opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            gerar_id_produto()
        elif opcao == '3':
            atualizar_produto()
        elif opcao == '4':
            print('opcao apagar doce')
        elif opcao == '5':
            listar_todos()
        else:
            print('Opção inválida, por favor escolha um número válido no menu')

            #for n in lista_menu:
            #    print(n)

def gerar_id_produto():
    if len(lista_menu) == 0:
        return 1
    lista_menu.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_menu[0].get("id") + 1

    return novo_id

def adicionar_produto():
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = input("Digite o preço do produto:\n")

    produto = {
        "id": gerar_id_produto(),
        "nome": nome_produto,
        "preço": float(preco_produto),
    }
    lista_menu.append(produto)

    print(lista_menu)

def atualizar_produto():
     id_produto = input("Digite o ID do produto para atualizar:\n")
     for index in range(len(lista_menu)):
        if lista_menu[index].get("id") == int(id_produto):
            novo_valor = input("Digite o novo valor do produto:\n")
            lista_menu[index]["preço"] = float(novo_valor)
            print(f"O produto foi atualizado com sucesso! {lista_menu[index]}")

def listar_todos():
    for index in range(len(lista_menu)):
        print(f"{lista_menu[index]}\n")

def exibir_detalhes():
    exibir_item = int(input("Digite a id:"))

    for index in lista_menu:  
        if exibir_item == index.get("id"): 
           print(f"{index}")

def delete():
    deletar_doce = int(input("Digite id que deseja deletar:"))

    for index in range(len(lista_menu)): 
        if index < len(lista_menu):     
            if lista_menu[index].get("id") == deletar_doce:
                lista_menu.pop(index)   
                print("O produto foi deletado com sucesso!")

menu()