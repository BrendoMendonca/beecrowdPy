n = int(input())

for i in range(1, n+1):
    print(i, end=' ')
    print(f"{pow(i,2):.0f}", end=' ')
    print(f"{pow(i,3):.0f}")

    print(i, end=' ')
    print(f"{1 + pow(i,2):.0f}", end=' ')
    print(f"{1 + pow(i,3):.0f}")