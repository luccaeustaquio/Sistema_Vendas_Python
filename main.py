
estoque_Sistema = {

    1:  {"Nome" : "💻Notebook gamer", "Preço" : 5.000,"Quantidade Estoque" : 15},
    2:  {"Nome" : "🎮Videogame (PS5, Xbox) ", "Preço" : 8.300 ,"Quantidade Estoque" : 20},
    3:  {"Nome" : "🖥️Monitor Gamer","Preço" : 4.500,"Quantidade Estoque" : 25},
    4:  {"Nome" : "💺Cadeira Gamer","Preço" :3.250, "Quantidade Estoque" : 15},
    5:  {"Nome" : "🎧Fone Bluetooth", "Preço" : 5.000,"Quantidade Estoque" : 10}

}

carrinho_Compras = []

while True:

    print("=="*15)
    print("Bem vindo a Loja Virtual")
    print("=="*15)

    print("[1] Visualizar Estoque")
    print("[2] Adicionar Item ao Carrinho")
    print("[3] Visualizar Carrinho")
    print("[4] Finalizar Compra")
    print("[0] Sair do Sistema")
    opcao = int(input("Digite a sua opçao desejada: "))

    match opcao :
        case 1:
            print("[1] = Visualizaçao Estoque: ")
            for codigo, produto in estoque_Sistema.items():

                print(f"\nCódigo: {codigo}")
                print(f"Nome: {produto['Nome']}")
                print(f"Preço: R$ {produto['Preço']}")
                print(f"Quantidade em estoque: {produto['Quantidade Estoque']}")

        case 2:
            print("[2] = Adicionar Item ao Carrinho:")

            compra = input("Código do Produto Desejado: ")

            for k,v in estoque_Sistema.items():
                if compra == k:
                    quantidade_Product = int(input(f"Quantos {v} ? "))
                    if v["Quantidade Estoque"] >= quantidade_Product:
                        carrinho_Compras.append(v)
                        print(f"{v} adicionado ao carrinho! ")
                        estoque_Sistema[v]["Quantidade Estoque"] -= quantidade_Product
                    else:
                        print("Estoque insuficiente! Nao é possível adicionar ao carrinho !😨")
                else :
                    print("Código inválido! Tente novamente!")

        case 3:
                print("[3] = Visualizaçao Carrinho de Compras :")
                if carrinho_Compras is None:
                  print("Seu Carrinho está vazio ☹️! Adicione algum Produto.")
                else:
                  print(carrinho_Compras)
                  subTotal_Carrinho = sum("Preço")
                  print(f"SubTotal da sua compra: {subTotal_Carrinho}")

        case 4:
            print("[4] = Finalizar Compra")









