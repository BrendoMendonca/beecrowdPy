a = [0.0] * 100
for i in range(0, 100):
    valor = float(input())
    a[i] = valor
for i in range(0, 100):
    if(a[i] <= 10):
        print(f"A[{i}] = {a[i]:.1f}")