o = input() #recebimento da operação
soma, quant = 0 #quant representa quantidade de elementos acimma da diagonal principal
matriz = [[] for _ in range(12)] #inicialização da matriz

for i in range(12):
    for j in range(12):
        matriz[i].append(float(input())) #recebimento dos valores da matriz
        if(j>i): #verificar se o valor está acima da diagonal da matriz
            soma += matriz[i][j]
            quant+=1
#exibição dos valores
if(o == 'S'):
    print(f"{soma:.1f}")
else:
    print(f"{soma/quant:.1f}")