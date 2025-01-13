import sys

def graus_para_horario(graus):
    #calcula o total de segundos no dia com base nos graus
    total_segundos = round((graus / 360) * 24 * 3600)

    #adiciona 6 horas (em segundos) para ajustar o início do dia
    total_segundos = (total_segundos + 6 * 3600) % (24 * 3600)

    #converte para horas, minutos e segundos
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60

    return f"{horas:02}:{minutos:02}:{segundos:02}"

def saudacao(horas):#função que exibe as mensagens de acordo com a hora
    if 6 <= horas < 12:
        return "Bom Dia!!"
    elif 12 <= horas < 18:
        return "Boa Tarde!!"
    elif 18 <= horas < 24:
        return "Boa Noite!!"
    else:
        return "De Madrugada!!"

def main():
    for linha in sys.stdin:
        try:
            graus = float(linha.strip())
            horario = graus_para_horario(graus)

            #extrai as horas do horário calculado
            horas = int(horario.split(":")[0])

            #determina a saudação
            periodo = saudacao(horas)

            #imprime a saudação e o horário
            print(periodo)
            print(horario)
        except ValueError:
            break

if __name__ == "__main__":
    main()
