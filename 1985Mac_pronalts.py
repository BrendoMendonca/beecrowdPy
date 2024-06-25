n = int(input())#recebimento da quantidade de produtos comprados
soma = 0#inicialmente a soma é zero
for i in range(n):#estrutura de repetição para receber o produto comprado e a quantidade de cada um
    prod, qnt = map(str, input().split())#código do produto e a quantidade
    #o valor do produto é o final do seu código somado 0.5
    calculo = (int(prod[3]) + 0.5) * int(qnt)#calculo da quantidade do produto e valor associado a ele
    soma += calculo#calculo total
print(f"{soma:.2f}")#exibição do resultado