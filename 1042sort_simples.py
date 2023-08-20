valores = input()#recebimento dos números
numeros = valores.split()#recebendo os números de forma separada
numeros = [int(num) for num in numeros] #convertendo os valores para inteiros na lista
numeros_crescente = sorted(numeros) #criando lista dos números ordenados
#exibição das listas
for n in numeros_crescente:
    print(n)
print()
for n in numeros:
    print(n)