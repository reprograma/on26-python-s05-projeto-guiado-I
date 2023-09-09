#criar um menu: adicionar item
#exibir detalhe do item
#atualizar item
#apagar item
#exibir todos itens 
list=[
    {'id': 2, 'name': 'CHEESE CAKE', 'preço': 6.0},                  #Do dicionário eu tirei e coloquei várias vezes
    {'id': 1, 'name': 'ISLAND SWEET', 'preço': 7.0},             # mas no final acabei deixando os dados para facilitar a interação clientexproduto
    {'id': 3, 'name': 'NORTHERN LIGTH', 'preço': 5.0}               
    ]  
def menu():
    while True:
        print(" \n Firu's Store \n")
        print("1-To add")
        print("2-Refresh")
        print("3-Delete")
        print("4 Show details")
        print("5-Show")
        print("0-Exit")
        option=input("Select the option 1/2/3/4/5/0- \n")
        print(option)
        #testando o input# print(option)
        if option == "1":
            to_add_product()
        elif option == "2":
            refresh_product()
        elif option == "3":
            delete_product()
        elif option == "4":
            show_details()
        elif option == "5":
            show_all()
        elif option == "0":                   
            print("To exit")
            break
        else:
            print("Invalid option, please use a valid option")


def to_add_product():                                     
    name_product= input("Enter product name=")
    price_product= int(input("enter the value of the product="))
    product = {"id":create_id(),"name":name_product,"preço": float(price_product)} #dict
        

    list.append(product) 
    print(list)

def create_id():
    if len(list) == 0:
        return 1
    list.sort(key=lambda product: product.get("id") , reverse= True) #revertendo a ordem do sort, por que lambda?
    new_id= list[0].get("id")+1 #extraindo o valor do dict
    return new_id

def refresh_product():                                        #optei por deixar o código igual pois usei como referência para 
    id_product = int(input("enter the product id to refresh\n")) #desenvolver as demais função
    for index in range(len(list)):
        if list[index].get("id") == int(id_product):
            new_value = float(input("New price=\n"))
            list[index]["price_product"] = float(new_value)
            print("The product has been updated successfuly")

def delete_product():                                        #Nessa parte eu tinha reparado que havia uma relação entre os comandos
    id_product= int(input("enter the product id to delete\n"))  #da atualização(feito em aula), então usei os comandos semelhantes para
    for product in list:                                      #desenvolver a função de deletar, fiz alguns ajustes na hora de chamar 
        if product.get("id")==int(id_product):               #os valores, no lugar de usar o index chamei a própia variável  dentro
            list.remove(product)                             # da lista, de forma mais sucinta.
            print("The product has been deleteded")
            return 
    print("Product not found")
   
   

def show_details():
    if len(list)==0:
        print ("The list is empty")
    else:
        id_product= int(input("enter the product id="))
    for product in list:
        if product.get("id")==int(id_product):
            print(f'Details of product {product}')

                       
def show_all():
    for index in range(len(list)):
        print(f"{list[index]}\n")

menu()



