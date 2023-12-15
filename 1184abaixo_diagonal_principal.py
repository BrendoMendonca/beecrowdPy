o = input() #armazena o tipo de operação desejado
matriz = [[]for _ in range(12)] #inicializa a matriz 12x12
soma = quant = 0 #inicialmente a soma e quantidade de elementos abaixo da diagonal principal é zero

for i in range(12):
    for j in range(12):
        matriz[i].append(float(input())) #recebimento dos valores na matriz
        if(i > j): #verifica se o elemento que esá sendo adicionado fica abaixo da diagonal principal
            soma += matriz[i][j] #incremento da soma de acordo com o valor do elemento
            quant += 1

#imprime a saída de acordo com a operação desejada
if(o == 'S'):
    print(f"{soma:.1f}")
else:
    print(f"{soma/quant:.1f}")
