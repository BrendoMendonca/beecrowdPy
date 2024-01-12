operacao = input()
matriz = [[]for _ in range(12)]
soma = quant = 0
aux = 1

for i in range(12):
    for j in range(12):
        matriz[i].append(float(input()))
        if(j < aux):
            soma += matriz[i][j]
            quant += 1
    if (i <= 6):
        aux += 1
    else:
        aux -= 1

if(operacao == 'S'):
    print(f"{soma:.1f}")
else:
    print(f"{soma/quant:.1f}")