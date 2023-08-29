valores = input()
a, b,c = map(float,valores.split())

if(a + b > c) and (a + c > b) and (b + c > a):#verifica as condições para os lados serem um triângulo
    perim = b + c + a
    print(f"Perimetro = {perim:.1f}")
else:
    area = ((a+b)*c)/2
    print(f"Area = {area:.1f}")