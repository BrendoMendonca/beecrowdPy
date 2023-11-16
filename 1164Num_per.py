n = int(input())

for _ in range(n):
    soma = 0        
    num = int(input())
    for i in range(1, num + 1):
        if(num % i == 0):
            soma += i
    if((soma - num) == num):
        print(f"{num} eh perfeito")
    else:
        print(f"{num} nao eh perfeito")