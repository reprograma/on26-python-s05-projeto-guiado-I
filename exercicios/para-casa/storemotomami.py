# A minha lista assim como um todo do meu código será baseado na discografia da Beyoncé.
# Simm, a loja da May é Beyhive e os valores é definido de acordo com as notas do metacrict de cada álbum.

#Irei manter a lista com as minhas modificações para fazer um sentido maior na minha cabeça.
list_of_candys = [{"id": 0, "name": "Dangerously in love", "value": 63.0}, {"id": 1, "name": "B'Day", "value": 70.0}, {"id": 2, "name": "I'am...Sasha Fierce", "value": 62.0}, {"id": 3, "name": "4", "value": 73.0}, {"id": 4, "name": "BEYONCÉ", "value": 85.0}, {"id": 5, "name": "Lemonade", "value": 92.0}, {"id": 6, "name": "Homecoming", "value": 95.0}, {"id": 7, "name": "The Gift", "value": 77.0}, {"id": 8, "name": "Renaissance", "value": 91.0}]

product_id = 1
def menu():
    while True:
        print("\n ** MENU STORE MAYHIVE **\n")
        print("1 - Add")
        print("2 - Show details")
        print("3 - Update")
        print("4 - Erase")
        print("5 - Show all")
        print("0 - Exit")

        option = input("Choose the option you want\n")

        if option == "1":
            add_product()
        elif option == "2":
            print("Detail of candy")
        elif option == "3":
            update_product()
        elif option == "4":
            erase_product()
        elif option == "5":
            list_all()
        elif option == "0":
            break
        else:
            print("Invalid option. Choose a option of menu")

def generate_product_id():
    if len(list_of_candys) == 0:
        return 1
    list_of_candys.sort(key=lambda product: product.get("id"), reverse=True)
    new_id = list_of_candys[0].get("id") + 1
    return new_id


def add_product():
    product_name = input("Type the name of product:\n")
    product_value = input("Type the value of product:\n")

    product = {
        "id": generate_product_id(),
        "name": product_name,
        "value": float(product_value),
    }
    list_of_candys.append(product)

    print(list_of_candys)


def update_product():
    product_id = input("Type the ID of product to update:\n")

    for index in range(len(list_of_candys)):
        if list_of_candys[index].get("id") == int(product_id):
            new_value = input("Type the new value of product:\n")
            list_of_candys[index]["value"] = float(new_value)
            print(f"Update success! {list_of_candys[index]}")


def list_all():
    for index in range(len(list_of_candys)):
        print(f"{list_of_candys[index]}\n")
        

def erase_product():
    del(list_of_candys[int(input("Choose a position:\n"))])

menu()


#Estava com dificuldade de fazer o erase rodar, fiquei feliz por conseguir, mas, temos um problema que eu não consegui resolver. hihi
#Eu comecei codando em inglês na oficina, mas estava me achando estranha durante as aulas por perceber que era a única, ao menos achava ser, mas, a Mirley fez eu ter vontade de voltar a codar em inglês. Creio que foi a maior "alteração" que fiz.
#Não fiz muitas alterações no seu código pelo motivo de; Está funcionando perfeitamente. Adoraria aperfeiçoar mas eu não estou apta ainda para isso. Mas ireim viu, Motomami.