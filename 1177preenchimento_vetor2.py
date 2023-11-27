t = int(input())
n = [0] * 1000
j = 0
for i in range(0, 1000):
    n[i] = j
    j +=1
    if(j == t):
       j = 0
    print(f"N[{i}] = {n[i]}")