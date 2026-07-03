cupom1 = str("DEV10")
cupom2 = str("DEV20")
subTotal_Carrinho = 0

estoque_Sistema = {

    1:  {"Nome" : "💻Notebook gamer", "Preco" : 5000.00,"Quantidade Estoque" : 15},
    2:  {"Nome" : "🎮Videogame (PS5, Xbox) ", "Preco" : 8.333 ,"Quantidade Estoque" : 20},
    3:  {"Nome" : "🖥️Monitor Gamer","Preco" : 4500.00 ,"Quantidade Estoque" : 25},
    4:  {"Nome" : "💺Cadeira Gamer","Preco" :3250.00, "Quantidade Estoque" : 15},
    5:  {"Nome" : "🎧Fone Bluetooth", "Preco" : 5650.00,"Quantidade Estoque" : 10}

}

carrinho_Compras = []
total_Compra = 0

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
                print(f"Preco: R$ {produto['Preco']}")
                print(f"Quantidade em estoque: {produto['Quantidade Estoque']}")

        case 2:
            print("[2] = Adicionar Item ao Carrinho:")

            compra = int(input("Código do Produto Desejado: "))

            if compra not in estoque_Sistema:
                    print("Código inválido!")

            else:

                for id_produto,valor in estoque_Sistema.items():

                    if compra == id_produto:
                        qtd_Product = int(input(f"Quantos {valor['Nome']} ? "))

                        if qtd_Product <= estoque_Sistema[id_produto]['Quantidade Estoque']:

                            item = {
                            "Quantidade" : qtd_Product,
                            "Nome" : estoque_Sistema[id_produto]['Nome'],
                            "Preco" : estoque_Sistema[id_produto]['Preco'],
                            "Preco_Total" : qtd_Product * estoque_Sistema[id_produto]['Preco']
                            }

                            carrinho_Compras.append(item)
                            estoque_Sistema[id_produto]['Quantidade Estoque'] -= qtd_Product

                            print(f"Produto {id_produto} adicionado ao carrinho! \n")
                            print(item)

                        else:
                         print(f"Nao é possível adicionar ao carrinho !😨. Temos apenas {estoque_Sistema[id_produto]['Quantidade Estoque']} no estoque.")
                        break;

        case 3:
                print("[3] = Visualizaçao Carrinho de Compras :")
                if carrinho_Compras is None:
                  print("Seu Carrinho está vazio ☹️! Adicione algum Produto.")
                else:
                  print(carrinho_Compras)
                  subTotal_Carrinho = sum(item["Preco"] for item in carrinho_Compras)
                  print(f"SubTotal da sua compra: {subTotal_Carrinho}")

        case 4:
            print("[4] = Finalizar Compra")

            if carrinho_Compras is None :
                print("Nao foi possível finalizar a compra! Seu carrinho está vazio.")

            tem_Cupom = str(input("Tem cupom ? S  ou  N")).upper()
            if tem_Cupom == "S":
                aplicar_Cupom = str(input("Digite o seu cupom: "))
                if aplicar_Cupom == cupom1:
                    total_Compra = subTotal_Carrinho * 0.10
                    print(f"🤑 Valor total com desconto:  : {total_Compra}")

                    print("Compra finalizada com sucesso!")
                    carrinho_Compras.clear()


                elif aplicar_Cupom == cupom2 and subTotal_Carrinho > 500 :
                    total_Compra = subTotal_Carrinho * 0.20
                    print(f"🤑 Valor total com desconto:  : {total_Compra}")
                else:
                    print("Este cupom só pode ser usado em compras superiores a R$500")

            else:
                print("Cumpom nao existe! ")











