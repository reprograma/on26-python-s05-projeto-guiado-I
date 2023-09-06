# Quero opção de:
# Adicionar doce
# Exibir detalhe de um doce
# Atualizar doce
# Apagar doces
# Exibir a lista de todos os doces

#Racíocionio pro exibir detalhes = "primeiro, mudar a ordem, fazer com que exibir todos venha antes, porque, na minha cabeça, os dois estão ligados. Primeiro ela exibe a lista,
# depois ela seleciona um dentro da lista exibida e então vai aparecer os detalhes do que foi selecionado.  #a escolha é por id? é possível eu criar um modo de, dentro desse detalhes,
# exibir os ingredientes ("contém lactose ou contém glúten")?? Mas e os ingredientes adicionais, como eu vou saber??
#Toda id segue um padrão, se eu padronizar, talvez consiga fazer o código exibir detalhes padrões pra id padrões.
#cancela, não sei fazer isso! ~ ACHO QUE CONSIGO SIM

import time

#Contém glútem = id é multiplo de 5
#Contém lactose = id é multiplo de 3
#Contém glútem e lactose = id é múltiplo de 7
#Sem lactose e sem glútem = outro


lista_produtos = [{'id': 3, 'nome': 'Brigadeiro', 'preço': 2.50}, {'id': 6, 'nome': 'Pudim', 'preço': 8.00}, {'id': 5, 'nome': 'Broa de fubá', 'preço': 0.50}, {'id': 7, 'nome': 'Rocambole', 'preço': 5.00}]
id_produto = 1
def menu():
    while True:
        print("\n ** MENU LOJA REPROGRAMA **\n")
        print("1 - Adicionar")
        print("2 - Exibir todos")
        print("3 - Atualizar")
        print("4 - Exibir detalhes")
        print("5 - Apagar")
        print("0 - Sair")

        opcao = input("Escolha a opção desejada\n")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_todos()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            detalhe_doce()
        elif opcao == "5":
            apagar_doce(produto=None)
        elif opcao == "0":
            break
        else:
            print("Opção inválida, por favor escolha uma opção do menu")

def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)
    ultimo_id = lista_produtos[0].get("id")
    
    pergunta1 = input("O produto contém glúten? Responda com 'sim' ou com 'não': ")
    pergunta2 = input("O produto contém lactose? Responda com 'sim' ou com 'não': ")
    novo_id = ultimo_id + 1
    #Deu errado inúmeras vezes porque eu tava usando novo_id*5, até a bonita lembrar que um múltiplo não é multiplicando 
    #mesmo assim não saiu como deveria, mas o importante foi o esforço
    if pergunta1 == "sim" and pergunta2 == "não":
        while novo_id % 5 == 0 or novo_id not in [35, 15, 70, 30, 45, 60, 75, 90]:
            novo_id += 1
        return novo_id
    elif pergunta1 == "sim" and pergunta2 == "sim":
        while novo_id % 7 == 0 or novo_id not in [35, 21, 70, 42, 63, 84]:
            novo_id += 1
        return novo_id
    elif pergunta1 == "não" and pergunta2 == "sim":
        while novo_id % 3 == 0 or novo_id not in [21, 42, 63, 84, 15, 30, 45, 60, 75, 90]:
            novo_id += 1
        return novo_id
    else:
        while novo_id % 8 == 0 or novo_id not in [40, 24, 56]:
            novo_id += 1
        return novo_id
def adicionar_produto():
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = input("Digite o preço do produto:\n")

    produto = {
        "id": gerar_id_produto(),
        "nome": nome_produto,
        "preço": float(preco_produto),
    }
    lista_produtos.append(produto)

    print(lista_produtos)

def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")

def atualizar_produto():
    id_produto = input("Digite o ID do produto para atualizar:\n")

    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("id") == int(id_produto):
            novo_valor = input("Digite o novo valor do produto:\n")
            lista_produtos[index]["preço"] = float(novo_valor)
            print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")


def detalhe_doce():
    try:
        id_doce = int(input("Digite o ID do produto que deseja ver os detalhes: "))
        for doce in lista_produtos:
            if doce['id']== id_doce:
                if id_doce % 5 == 0 and id_doce not in["35", "15", "70", "30", "45", "60", "75", "90"]:
                    print(f'Id do produto: {id_doce}:')
                    print(f'Nome: {doce["nome"]}')
                    print(f'Preço: R${doce["preço"]:.2f}')
                    print("Esse doce contém glútem e não contém lactose!")
                
                elif id_doce % 7 == 0 and id_doce not in ["35", "21", "70", "42", "63", "84"]:
                    print(f'Id do produto: {id_doce}:')
                    print(f'Nome: {doce["nome"]}')
                    print(f'Preço: R${doce["preço"]:.2f}')
                    print("Esse doce contém glútem e contém lactose!")
            
                elif id_doce % 3 == 0 and id_doce not in ["21", "42", "63", "84", "15", "30", "45", "60", "75", "90"]:
                    print(f'Id do produto: {id_doce}:')
                    print(f'Nome: {doce["nome"]}')
                    print(f'Preço: R${doce["preço"]:.2f}')
                    print("Esse doce não contém glútem e contém lactose!")
            
                elif id_doce % 8 == 0 and id_doce not in ["40", "24", "56"]:
                    print(f'Id do produto: {id_doce}:')
                    print(f'Nome: {doce["nome"]}')
                    print(f'Preço: R${doce["preço"]:.2f}')
                    print("Esse doce não contém glútem e não contém lactose!")
                    return
                else:
                    print("O produto não foi encontrado na lista.")

    except ValueError:
        print("Por favor, digite um ID válido.")

def apagar_doce(produto):
    #vou tentar usar o try e except porque possui mais potencial de dar erro nesse
    try:
        id_doce_apagar = int(input("Digite o ID do produto que deseja apagar: "))
        if produto['id'] == id_doce_apagar:
                produto_achado = produto
        if produto_achado:
            lista_produtos.remove(produto_achado)
            print("O produto foi apagado com sucesso.")
        else:
            print("O produto não foi encontrado na lista.")

    except ValueError:
        print("Por favor, digite um ID válido.")
    return


menu()


