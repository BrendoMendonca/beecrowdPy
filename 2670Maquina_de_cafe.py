#recebimento da quantidade de funcionários por andar
andar1 = int(input())
andar2 = int(input())
andar3 = int(input())

#calculo de tempo gasto em cada andar
tempo_andar1 = andar3*4 + andar2*2
tempo_andar2 = andar1*2 + andar3*2
tempo_andar3 = andar1*4 + andar2*2
#verifica e imprime o menor tempo
tempo_min = min(tempo_andar1, tempo_andar2, tempo_andar3)
print(tempo_min)