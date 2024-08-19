from math import sqrt#importação da função sqrt para calcular a raiz quadrada
n = int(input())#recebimento do valor
#cálculo do Fibonacci 
fib = ((((1+sqrt(5))/2)**n) - ((1-sqrt(5))/2)**n)/sqrt(5)
#exibição do resultado
print(f"{fib:.1f}")