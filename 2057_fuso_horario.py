saida, tempo, fuso = map(int, input().split())#recebimento dos valores
horario = saida

#calculo do horário de chegada
horario = saida + tempo + fuso
#ajuste do valor do valor do horário chegada de acordo com o fuso
if(horario > 24):
    horario -= 24
if(horario < 0):
    horario += 24

#exibição do resultado
print(horario)