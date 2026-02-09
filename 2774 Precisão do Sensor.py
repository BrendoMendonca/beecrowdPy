from math import sqrt
while True:
    try:
        h, m = map(int, input().split())
        valores =list(map(float, input().split()))#valores de medição do sensor
        media = sum(valores)/len(valores)
        somatorio = 0
        for i in range(len(valores)):
            somatorio += ((valores[i] - media)**2)
        precisao = sqrt(somatorio/(len(valores)-1))#calculo da presição de acordo com a fórmula apresentada

        print(f"{precisao:.5f}")
    except EOFError:
        break