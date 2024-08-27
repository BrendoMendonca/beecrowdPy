n = int(input())#recebimento da quantidade de quadras-1

quadras = []#inicia a lista de quadras
for i in range(n+1):#estrutura de repetição para recebimento dos valores das quadras
    linha = list(map(int, input().split()))
    quadras.append(linha)
        
for i in range(n):#estrutura de repetição para verificar se as quadras são seguras 
    for j in range(n):
        if(quadras[i][j] + quadras[i][j+1] + quadras[i+1][j] + quadras[i+1][j+1]) >=2:#verifica se a quadra possui 2 ou mais cameras ativas
            print("S", end='')
        else:
            print("U", end='')
    print()