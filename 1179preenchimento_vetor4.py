#listas para armazenar os valores pares e impares
par = []
impar = []

for i in range(0, 15):
    valor = int(input())#recebimento dos valores
    #verifica se o valor recebido é par ou impar e adiciona a lista correspondente
    if(valor % 2 == 0):
        par.append(valor)
    else:
        impar.append(valor)
    
    #verifica se uma das listas já possui 5 valores, a exibe e esvazia a lista novamente para recebimento de novos valores
    if(len(par) == 5):
        for j in range(0, len(par)):
            print(f"par[{j}] = {par[j]}")
        par = []

    if(len(impar) == 5):
        for j in range(0, len(impar)):
            print(f"impar[{j}] = {impar[j]}")
        impar = []

#exibição das listas com os valores restantes
for i in range(0, len(impar)):
    print(f"impar[{i}] = {impar[i]}")

for i in range(0, len(par)):
            print(f"par[{i}] = {par[i]}")