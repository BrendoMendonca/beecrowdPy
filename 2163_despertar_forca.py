n_linha, n_coluna = map(int, input().split())
matriz = []
x = y = 0
for i in range(n_linha):
    valores = input()
    linha = [int(num) for num in valores.split()]
    matriz.append(linha)
    
for i in range(1, n_linha-1):
    for j in range(1, n_coluna-1):
        if(matriz[i][j] == 42):
            if(matriz[i-1][j-1] == matriz[i-1][j] == matriz[i-1][j+1]
               == matriz[i][j-1] == matriz[i][j+1]
               == matriz[i+1][j-1] == matriz[i+1][j] == matriz[i+1][j+1] == 7):
                x = i
                y = j
if(x or y != 0):
    print(f"{x+1} {y+1}")
else:
    print(f"{x} {y}")