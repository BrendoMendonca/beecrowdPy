a, b, c = map(int, input().split())# recebimento das temperaturas

#verificação de cada situação
if(a > b) and (b <= c):
    print(":)")
elif(a < b) and (b >= c):
    print(":(")
elif (b - a > c - b):
    print(":(")
elif (b - a <= c - b and b > a):
    print(":)")
elif(a-b > b-c):
    print(":)")
elif(a-b >= b-c):
    print(":(")
elif(a == b):
    if(b < c):
        print(":)")
    else:
        print(":(")