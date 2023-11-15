#recebimento de valores
x = int(input())
z = int(input())

#recebimento do valor de z até que seja informado um valor maior que x
while(x >= z):
    z = int(input())

#a soma dos valores parte de x
soma = x

#a quantidade de valores recebe 1, pois a soma parte de x, então já tem um valor incluso
quant = 1

#cálculo da quantidade de valores necessários para sua soma ser maior que z
for i in range(x, z + 2):
    soma += i
    quant += 1
    if(soma > z):
        break

print(quant)