def calcular_diferenca_otima(n, trabalhos):
    soma_total = sum(trabalhos)
    soma_rangel = 0
    menor_diferenca = float('inf')

    for i in range(n - 1): #rangel não pode fazer todos os trabalhos
        soma_rangel += trabalhos[i]
        soma_gugu = soma_total - soma_rangel
        diferenca = abs(soma_rangel - soma_gugu)
        menor_diferenca = min(menor_diferenca, diferenca)

    return menor_diferenca

while True:
    try:
        #recebe o número de elementos na sequência
        n = int(input().strip())
        #recebe os elementos da sequência
        trabalhos = list(map(int, input().strip().split()))
        #calcula a diferença ótima
        resultado = calcular_diferenca_otima(n, trabalhos)
        #exibe o resultado
        print(f"{resultado}")
    except EOFError:
        break