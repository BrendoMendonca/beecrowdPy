while True:
    try:
        grau = int(input()) #recebimento do ângulo
        
        #verifica em que ângulo está e exibe o resultado
        if (grau >= 0 and grau < 90) or (grau == 360):
            print("Bom Dia!!")
        elif (grau >= 90 and grau < 180):
            print("Boa Tarde!!")
        elif(grau >= 180 and grau < 270):
            print("Boa Noite!!")
        else:
            print("De Madrugada!!")
        
    except EOFError:
        break