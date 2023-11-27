n = [0] * 10
valor = int(input())
for i in range(0,10):
    n[i] = valor
    valor *= 2
    print(f"N[{i}] = {n[i]}")