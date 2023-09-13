# recebimento das informações de entrada
dia_inicio = input().split()
hora_inicio = input().split(" : ")
dia_termino = input().split()
hora_termino = input().split(" : ")

# conversão de valores para inteiros
dia_inicio = int(dia_inicio[1])
hora_inicio = list(map(int, hora_inicio))
dia_termino = int(dia_termino[1])
hora_termino = list(map(int, hora_termino))

# calculo da diferença de dias
diferenca_dias = dia_termino - dia_inicio

# calculo da diferença de horas, minutos e segundos
segundos_inicio = hora_inicio[0] * 3600 + hora_inicio[1] * 60 + hora_inicio[2]
segundos_termino = hora_termino[0] * 3600 + hora_termino[1] * 60 + hora_termino[2]
diferenca_segundos = segundos_termino - segundos_inicio

# verifica se a diferença de segundos seja sempre positiva
if diferenca_segundos < 0:
    diferenca_segundos += 86400  # 86400 segundos em um dia (24 horas * 60 minutos * 60 segundos)
    diferenca_dias -= 1

# calcula a duração total em dias, horas, minutos e segundos
dias = diferenca_dias
horas = diferenca_segundos // 3600
diferenca_segundos %= 3600
minutos = diferenca_segundos // 60
segundos = diferenca_segundos % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
