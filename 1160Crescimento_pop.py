#número de casos de teste
T = int(input())

#loop através dos casos de teste
for _ in range(T):
    #entrada para cada caso de teste
    PA, PB, G1, G2 = map(float, input().split())

    #converte populações para inteiros
    PA, PB = int(PA), int(PB)

    #inicializa a variável para armazenar o número de anos
    anos = 0

    #loop para calcular o tempo em anos para A ultrapassar B em população
    while PA <= PB:
        PA += int(PA * (G1 / 100))
        PB += int(PB * (G2 / 100))
        anos += 1

        #verifica se o tempo é mais do que 100 anos
        if anos > 100:
            print("Mais de 1 seculo.")
            break
    else:
        #se o loop terminar sem atingir mais de 100 anos, imprime o resultado
        print(f"{anos} anos.")
