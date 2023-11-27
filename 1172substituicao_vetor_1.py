vetor = [0] * 10 #inicialização do vetor com 10 elementos de valor 0

#estruura de repetição para receber os valores do usuário
for i in range(0,10):
    valor = int(input())
    if(valor <= 0):
        vetor[i] = 1
    else:
        vetor[i] = valor

#exibição dos valores
for i in range(0, 10):
    print(f"X[{i}] = {vetor[i]}")