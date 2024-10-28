def vizinhos(borda, n, m, i, j):#funcao para verificar os vizinhos de cada célula e conta quantos paes de queijo tem em seus vizinhos
    count = 0
    #verifica a parte superior
    if i > 0 and borda[i-1][j] == 1:
        count += 1
    #verifica a parte inferior
    if i < n-1 and borda[i+1][j] == 1:
        count += 1
    #verifica a esquerda
    if j > 0 and borda[i][j-1] == 1:
        count += 1
    #verifica a direita
    if j < m-1 and borda[i][j+1] == 1:
        count += 1
    return count

def process_borda(n, m, borda):#verifica as bordas da matriz
    result = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if borda[i][j] == 1:
                result[i][j] = 9
            else:
                result[i][j] = vizinhos(borda, n, m, i, j)
    
    return result

def main():
    try:
        while True:
            n, m = map(int, input().split())
            borda = [list(map(int, input().split())) for _ in range(n)]
            result = process_borda(n, m, borda)
            
            for linha in result:
                print("".join(map(str, linha)))
    except EOFError:
        pass

if __name__ == "__main__":
    main()
