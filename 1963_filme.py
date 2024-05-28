valor1, valor2 = map(float, input().split())#recebimento dos valores
aumento = abs((valor1-valor2)/valor1*100)#cálculo do aumento do preço
print(f"{aumento:.2f}%")#exibição do resultado
