a, b, c = map(int, input().split())#recebimento dos lados

if(a < b + c and b < a + c and c < a + b):#verifica se os lados formam um triangulo
    #verifica qual tipo de triangulo os lados formam
    if(a == b and b == c):
        print("Valido-Equilatero")
    elif(a != b and b != c and a != c):
        print("Valido-Escaleno")
    else:
        print("Valido-Isoceles")
    #verifica se o triangulo é retangolo
    if(c**2 == a**2 + b**2):
        print("Retangulo: S")
    else:
        print("Retangulo: N")
else:
    print("Invalido")