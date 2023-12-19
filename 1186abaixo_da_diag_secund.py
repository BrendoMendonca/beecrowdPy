o = input() #recebimento da operação
matriz = [[]for _ in range(12)] #inicialização da matriz
soma = quant = 0 #inicialmente a soma e a quantidade de valores acima da diagonal secundária é zero

for i in range(12):
    for j in range(12):
        matriz[i].append(float(input()))#recebimento dos valores da matriz
        if(j <= (10 - i)): #verifica se a posição atual está acima da diagonal secundária
            soma += matriz[i][j]
            quant += 1

#exibe o resultado de acordo com a operação escolhida
if(o == 'S'):
    print(f"{soma:.1f}")
else:
    print(f"{soma/quant:.1f}")
    