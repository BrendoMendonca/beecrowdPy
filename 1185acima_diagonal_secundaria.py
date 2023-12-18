o = input()
matriz = [[]for _ in range(3)]
soma = quant = 0

for i in range(3):
    for j in range(3):
        matriz[i].append(float(input()))
        if(j <= (1 - i)):
            soma += matriz[i][j]
            quant += 1

if(o == 'S'):
    print(f"{soma:.1f}")
else:
    print(f"{soma/quant:.1f}")