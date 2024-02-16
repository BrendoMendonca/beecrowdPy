while(True):
    n = int(input())#recebimento da ordem da matriz
    if(n == 0):#verifica o critério de parada
        break
    matriz = [[0] * n for _ in range(n)]#inicialização da matriz

    for i in range(n):
        for j in range(n):
            matriz[i][j] = abs(i - j) + 1 #recebimento dos valores da matriz

    for i in range(n): #exibição da matriz de acordo com as especificações
        for j in range(n):
            print(f"{matriz[i][j]:>3}", end="")
            if(j < (n-1)):
                print(" ", end="")
        print()
    print()