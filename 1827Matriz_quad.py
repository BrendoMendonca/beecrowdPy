while(True):
    try:
        n = int(input())#recebimento da ordem da matriz
        central = int (n/2)#posição do elemento central
        posicao_1 = int(n/3)#posição de início e fim do número 1

        matriz = [[0] * n for _ in range(n)]#inicialização da matriz com 0

        for i in range(n):
            for j in range(n):
                if(j == i):#preenchimento da diagonal principal
                    matriz[i][j] = 2
                if(j==n-i-1):#preenchimento da diagonal secundária
                    matriz[i][j] = 3

        for i in range(posicao_1, n - posicao_1):#preenchimento do valor 1
            for j in range(posicao_1, n - posicao_1):
                matriz[i][j] = 1


        matriz[central][central] = 4#inserção do valor central

        for i in range(n):#exibição da matriz
            for j in range(n):
                if(j==n-1):
                    print(matriz[i][j])
                else:    
                    print(matriz[i][j], end="")
        print()
    except EOFError:
        break