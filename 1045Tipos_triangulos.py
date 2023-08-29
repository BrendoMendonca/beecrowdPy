valores = input()#recebimento dos números
numeros = valores.split()#recebendo os números de forma separada
numeros = [float(num) for num in numeros] #convertendo os valores para inteiros na lista
numeros = sorted(numeros, reverse=True) #ordenando a lista d eforma dcrescente

a = numeros[0]
b = numeros[1]
c = numeros[2]

if a>=(b+c):
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == (b**2 + c**2):
        print("TRIANGULO RETANGULO")
    if (a**2 > (b**2 + c**2)):
        print("TRIANGULO OBTUSANGULO")
    if a**2 < (b**2 + c**2):
        print("TRIANGULO ACUTANGULO")
    if a==b and b==c and a==c:
        print("TRIANGULO EQUILATERO")
    if a==b or b==c or a==c:
        print("TRIANGULO ISOSCELES")