valores = input()
x, y = map(int, valores.split())
n = 1
for i in range(0, y, x):
    for j in range(0, x):
        if j != x-1:          
            print(f"{n} ", end='' )
        else:
            print(f"{n}", end='')
        n += 1
    print()