n = int(input())#recebimento do valor

aux = 1 #variável auxiliar para controlar a impressão dos números

for i in range(0, n):#laço para controlar a quantidade de linhas impressas
    for j in range(aux, aux + 3): #laço para impressão dos números que vai do valor da variável auxiliar até a própria variável + 3
        print(j, end=' ') #exibição das linhas
    print("PUM") #exibição do final de cada linha
    aux = j + 2 #incremento da varivável auxiliar para seguir a sequencia de números