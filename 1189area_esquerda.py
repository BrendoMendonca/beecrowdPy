operacao = input() #recebimento do tipo de operação
matriz = [[]for _ in range(12)] #inicialização da matriz
soma = quant = 0 #inicialmente, a soma e a quantidade de elementos da esquerda é 0
aux = 0 #variável auxiliar para verificar se elementos da matriz fazem parte da esquerda

for i in range(12):
    for j in range(12):
        matriz[i].append(float(input()))#inserção dos elementos na matriz
        if(j < aux):#verifica se a posição do elemento adicionado faz parte da esquerda
            #incrementação da soma e quantidade de elementos
            soma += matriz[i][j]
            quant += 1
    #incremento da variável auxiliar de acordo com as condições da área esquerda
    if (i < 5):
        aux += 1
    if(i >= 6):
        aux -= 1
#impressão dos resultados
if(operacao == 'S'):
    print(f"{soma:.1f}")
else:
    print(f"{soma/quant:.1f}")