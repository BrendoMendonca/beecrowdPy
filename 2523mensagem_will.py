while(True):
    try:
        #recebimento dos valores de entrada
        letras = input().upper()
        n = int(input())
        lampadas = input().split()
        #verifica cada caractere da string e imprime as que possuem indice correspondente
        for caractere in lampadas:
            print(letras[int(caractere)-1], end="")
        print()
    except EOFError:
        break