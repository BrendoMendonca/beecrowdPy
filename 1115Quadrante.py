while True:
    valores = input() #recebimento dos valores
    x, y = map(int, valores.split()) #atribuição dos valores para as varáveis

    #testes condicionais para verificar em qual quadrante pertence as coordenadas
    
    if(x == 0 or y == 0):
        break

    if(x > 0 and y > 0):
        print("primeiro")

    elif(x > 0 and y < 0):
        print("quarto")
    
    elif(x < 0 and y > 0):
        print("segundo")

    elif(x < 0 and y < 0):
        print("terceiro")