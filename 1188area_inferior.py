o = input()#recebimento do tipo de operação
matriz = [[] for _ in range(12)] #incialização da matriz
soma = quant = 0 #inicialmente a soma e a quantidade de elementos na área inferior é 0

#funções auxiliares para verificar se os elementos adicionamos na matriz estão na área inferior
auxA = 4
auxB = 7

for i in range(12):
    for j in range(12):
        matriz[i].append(float(input())) #recebimento dos valores da matriz
        if (j > auxA and j < auxB and i > 6): #verifica se o elemento adiciona faz parte da área inferior
            soma += matriz[i][j]
            quant +=1
    if(i > 6):#as variáveis auxiliares só serão incrementadas se o i for maior que 6(parte inferior)
        auxA -=1
        auxB +=1
#impressão dos valores
if(o == 'S'):
    print(f"{soma:.1f}")
else:
    print(f"{soma/quant:.1f}")