n = int(input())
dentro = 0

def intervalo(x):
    for i in range(10, 21):
        if(x == i):
            return 1
    return 0

for i in range (0, n):
    x = int(input())
    dentro += intervalo(x)

fora = (n - dentro)

print(f"{dentro} in")
print(f"{fora} out")
