while True:
    valores = input() #recebimento dos valores
    x, y = map(int, valores.split()) #atribuição dos valores para as varáveis

    if(x == y):
        break
    if(x > y):
        print("Decrescente")
    else:
        print("Crescente")