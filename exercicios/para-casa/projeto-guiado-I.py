class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.items = {}

    def adicionar_item(self, produto, quantidade):
        if produto.id in self.items:
            self.items[produto.id] += quantidade
        else:
            self.items[produto.id] = quantidade

    def remover_item(self, id):
        if id in self.items:
            del self.items[id]

    def calcular_total(self, catalogo_produtos):
        total = 0
        for id, quantidade in self.items.items():
            produto = catalogo_produtos[id]
            total += produto.preco * quantidade
        return total

def exibir_catalogo(catalogo_produtos):
    print("Catálogo de Produtos:")
    for produto in catalogo_produtos.values():
        print(f"{produto.id}: {produto.nome} - R${produto.preco:.2f}")

def main():
   
    catalogo_produtos = {
        1: Produto(1, "Base", 10.99),
        2: Produto(2, "Batom", 5.49),
        3: Produto(3, "Rímel", 7.99),
    }

    carrinho = Carrinho()

    while True:
        print("\nMenu:")
        print("1. Adicionar produto ao carrinho")
        print("2. Remover produto do carrinho")
        print("3. Ver total do carrinho")
        print("4. Finalizar compra")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            exibir_catalogo(catalogo_produtos)
            id = int(input("Digite o id do produto: "))
            quantidade = int(input("Digite a quantidade desejada: "))
            produto = catalogo_produtos.get(id)
            if produto:
                carrinho.adicionar_item(produto, quantidade)
                print(f"{quantidade} {produto.nome}(s) adicionado(s) ao carrinho.")
            else:
                print("Produto não encontrado.")

        elif opcao == "2":
            id = int(input("Digite o id do produto a ser removido: "))
            carrinho.remover_item(id)
            print("Produto removido do carrinho.")

        elif opcao == "3":
            total = carrinho.calcular_total(catalogo_produtos)
            print(f"Total do carrinho: R${total:.2f}")

        elif opcao == "4":
            total = carrinho.calcular_total(catalogo_produtos)
            if total > 0:
                print(f"Compra finalizada! Número do pedido: {hash(carrinho)}")
                print(f"Total da compra: R${total:.2f}")
                break
            else:
                print("Carrinho vazio. Adicione produtos antes de finalizar a compra.")

        elif opcao == "5":
            print("Saindo do programa. Obrigado!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()