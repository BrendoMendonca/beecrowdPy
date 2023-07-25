linha1 = input()
cod1, num1, valor1 = map(float, linha1.split())

linha2 = input()
cod2, num2, valor2 = map(float, linha2.split())

total = (num1 * valor1) + (num2 * valor2)

print(f"VALOR A PAGAR: R$ {total:.2f}")