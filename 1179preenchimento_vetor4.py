par = []
impar = []

for i in range(0, 5):
    valor = int(input())
    if(valor % 2 == 0):
        par.append(valor)
    else:
        impar.append(valor)

    if(len(par) == 5):
        for j in range(0, len(par)):
            print(f"par[{j}] = {par[j]}")