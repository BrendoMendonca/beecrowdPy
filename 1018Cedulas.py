n = int(input())
print(n)
cedulas = [100, 50, 20, 10, 5, 2, 1]#lista com cédulas disponíveis
quant_cedula = {} #dicionario que armazena a quantidade de cada nota

for cedula in cedulas:
    quant = n // cedula
    n = n % cedula
    quant_cedula[cedula] = quant

for cedula, quantidade in quant_cedula.items():
    print(f"{quantidade} nota(s) de R$ {cedula},00")