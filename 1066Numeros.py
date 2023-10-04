par = impar = positivo = negativo = 0

for i in range (0, 5):

    num = float(input())
    if(num > 0):
        positivo +=1
    if(num < 0):
        negativo +=1
    if(num % 2 != 0):
        impar += 1
    if(num % 2 == 0):
        par += 1

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")