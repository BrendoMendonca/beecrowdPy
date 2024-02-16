while True:
    try:
        n = int(input())#recebe a ordem da matriz
        matriz = [[3] * n for _ in range(n)] #inicializa a matriz com o valor 3 em todas as posições

        #laço para percorrer a matriz
        for i in range(n):
            for j in range(n):                   
                matriz[i][i] = 1 #em cada linha, é adicionado o valor 1 na posição que contém o mesmo valor de linha e coluna
                matriz[i][n-i-1] = 2#em cada linha, é adicionado o valor 2 na posição n-i-1
        
        for row in matriz:
            print("".join(map(str, row)))#impressão da matriz de acordo com as especificações
    except EOFError:
        break