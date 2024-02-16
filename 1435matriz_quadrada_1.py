def construir_matriz(n): #função que inicializa e preenche a matriz
    matriz = [[0] * n for _ in range(n)] #inicialização da matriz de ordem n preenchida com 0

    for i in range(n):
        for j in range(n):
            matriz[i][j] = min(i, j, n-1-i, n-1-j) + 1 #preenche a matriz com o menor valor entre os parâmetros de "min" e soma + 1 - isso representa a menor distancia ao centro da mtriz

    return matriz

while True:
    n = int(input()) #recebimento do valor de ordem da matriz
    
    if n == 0: #critério de parada de recebimento de valores
        break
    
    matriz = construir_matriz(n) #chamda da função

    for i in range(n):#exibição da matriz de acordo com as especificações
        for j in range(n):
            print(f"{matriz[i][j]:>3}", end="")
            if j < n - 1:
                print(" ", end="")
        print()

    print()