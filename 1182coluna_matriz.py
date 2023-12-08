c = int(input()) #recebimento da coluna que será trabalhada
t = input() #caractere que representa a operação que será realizada
soma = 0 #inicialmente a soma é zero
matriz = [[] for _ in range(12)] #inicialização da matriz

for i in range(12):
    for j in range(12):
        matriz[i].append(float(input()))#recebimento dos valores da matriz

        if(c == j):#verifica se o valor de j é igual da coluna informada
            soma += matriz[i][j]#operação
#exibi a operação solicitada
if(t == 'S'):
    print(f"{soma:.1f}")
else:
    print(f"{soma/12:.1f}")