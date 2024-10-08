while True:
    try:
        n_treino = int(input())#recebimento da quantidade de treinos
        recorde = 0
        for i in range(n_treino):
            tempo, distancia = map(int, input().split())#recebimento do tempo e distancia do treino
            #calculo da velocidade
            velocidade = distancia/tempo
            if velocidade > recorde: #verifica se a velocidae é maior que a velocidade
                print(i+1)#exibe o número da volta que o recorde foi batido
                recorde = velocidade
    except EOFError:
        break