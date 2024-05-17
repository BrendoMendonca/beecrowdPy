n = int(input())#recebimento da qunatidade de casos teste
for i in range(n):
    valor = int(input())#recebimento da quantidade de termos
    if(valor % 2 == 0):#usando a lógica, se a quantidade de termos for ímpar o resultado será 1, caso contrário 0
        print(0)
    else:
        print(1)