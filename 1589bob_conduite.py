n = int(input())#recebimento da quantidade de casos
for i in range(n):
    valores = input()#recebimento dos valores dos raios
    r1, r2 = map(int, valores.split())
    print(r1+r2) #exibição do resultado