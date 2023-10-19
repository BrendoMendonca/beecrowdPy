n = int(input())

for i in range(n):
    valores = input()
    x, y = map(int, valores.split())

    if(y == 0):
        print("divisao impossivel")
    
    else:
        divisao = x/y
        print(f"{divisao:.1f}")