n = [0] * 20

for i in range(0, 20):
    valor = int(input())
    n[i] = valor

j = 19
for i in range(0, 10):
    
    aux = n[i]
    n[i] = n[j]
    n[j] = aux
    j -= 1

for i in range(0, 20):
    print(f"N[{i}] = {n[i]}")