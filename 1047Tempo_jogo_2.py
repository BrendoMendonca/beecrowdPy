# leitura dos tempos
hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

# calculo da diferença em minutos entre o horário final e o horário inicial
diferenca_minutos = (hora_final * 60 + minuto_final) - (hora_inicial * 60 + minuto_inicial)

#garante que a duração é no mínimo 1 minuto e no máximo 24 horas
if diferenca_minutos <= 0:
    diferenca_minutos += 24 * 60

#calculo as horas e minutos da duração
horas = diferenca_minutos // 60
minutos = diferenca_minutos % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")