x = int(input())
cont = 0

if(x % 2 == 0):
    x += 1

while(cont <= 5):
    print(x)
    x += 2
    cont += 1