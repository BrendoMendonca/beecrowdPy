valores = input()
a, b = map(float, valores.split())

if (b%a==0 or a%b==0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")