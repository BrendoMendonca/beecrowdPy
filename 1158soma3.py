n = int(input())#recebimento da quanitdade de casos

for i in range(0, n):
    valores = input()#recebimento dos valores
    x, y = map(int, valores.split())#conversão dos valores para int

    soma = 0 #para cada caso, a soma inicia zerada
    if(x % 2 == 0): #verifica se x é par e adiciona +1 ao valor caso seja par para se tornar um número ímpar
        x += 1

    for j in range(0, y):#cálulos da soma de ímpares
        soma += x
        x += 2
    print(soma)