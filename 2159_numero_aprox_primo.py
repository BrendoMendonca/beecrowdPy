from math import log#importação da função log para cálculo do log de n
n = int(input())#recebimento de n
#cálculos de p e m
p = n/log(n)
m = 1.25506*n/log(n)
#exibição do resultado
print(f"{p:.1f} {m:.1f}")