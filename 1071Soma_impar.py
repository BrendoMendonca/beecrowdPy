#entrada de dados
x = int(input())
y = int(input())
soma = 0
#verifica se os valores são iguas e imprime 0
if x == y:
    print(0)
#identificação do menor e maior valor para facilitar o cálculo
else:
    if(x < y):
        menor = x
        maior = y
    else:
        menor = y
        maior = x

    menor += 1 #o valor menor é incrementado para que não seja verificado no laço de repetção

    for i in range(menor, maior):
        if(i % 2 != 0):
            soma += i
    print(soma)