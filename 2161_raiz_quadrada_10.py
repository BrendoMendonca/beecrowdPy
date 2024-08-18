n = int(input())#recebimento da quantidade de repetições
inteiro = 3.0#valor da parte inteira da fórmula
fracao = 1/6#fração da fórmula
#verifica os casos padões 0 ou 1
if n == 0:
    print(f"{inteiro:.10f}")
elif n == 1:
    print(f"{inteiro+fracao:.10f}")
#caso o número de repetições não for 0 ou 1
else:
    den = 6 + fracao #valor do denominador inicial
    for i in range(n-1):#estrutura de reptição com decremento de -1 na condição de parada para a quantidade de repetiççoes ficar exata nos cálculos
        calculo = 6 + 1/den#calcula a cada repetição o valor
        den = calculo#calculo do novo denominador a cada repetição
    
    den = den - 6#ajuste no valor da parte inteira do denominador 
    print(f"{inteiro+den:.10f}")#exibição do resultado