x = float(input())
n = [0]*100


for i in range(0, 100):
    n[i] = x
    x = x/2
    print(f"N[{i}] = {n[i]:.4f}")