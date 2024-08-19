n_linha, n_coluna = map(int, input().split())#recebimento da quantidade de linhas e colunas
matriz = []#criação da matriz
x = y = 0#inicialmente os valores das coordenadas X Y são zero 

for i in range(n_linha):#estrutra de repetição para recebimento dos valores da matriz
    linha = list(map(int, input().split()))
    matriz.append(linha)
#estrutura de repetição para percorrer a matriz e verificar os valores    
for i in range(1, n_linha-1):
    for j in range(1, n_coluna-1):
        #verifica se os valores estão no padrão desejado
        if(matriz[i][j] == 42):
            if (matriz[i-1][j-1] == 7 and matriz[i-1][j] == 7 and matriz[i-1][j+1] == 7 and
                matriz[i][j-1] == 7 and matriz[i][j+1] == 7 and
                matriz[i+1][j-1] == 7 and matriz[i+1][j] == 7 and matriz[i+1][j+1] == 7):
                #atribuição dos valores das coordenadas
                x = i
                y = j
#exibição dos resultados
if(x or y != 0):
    print(f"{x+1} {y+1}")
else:
    print(f"{x} {y}")