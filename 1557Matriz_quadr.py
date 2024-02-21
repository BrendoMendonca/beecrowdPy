while True:
    n = int(input()) #recebimento do valor da ordem da matriz
    if n == 0:
        break
    
    matriz = [[0] * n for _ in range(n)] #inicialização da matriz
    valor = 1 #o valor do primeiro elemento da matriz

    for i in range(n):
        for j in range(n):
            matriz[i][j] = valor #preenchimento da matriz
            valor *= 2 #incrementação do valor(cada valor seguinte em uma linha é o dobro do valor atual)
        valor = 2 * matriz[i][0]#cada primeiro valor de uma linha é o dobro do primeiro elemento da lonha anterior

    maior = matriz[n-1][n-1] #maior valor da matriz
    tamanho = len(str(maior)) #verifica o tamanho do maior valor

    for i in range(n):
        for j in range(n):
            print(f"{matriz[i][j]:>{tamanho}}", end="")#impressão da matriz de acordo com as especificações 
            if j < n - 1:
                print(" ", end="")
        print()

    print()
