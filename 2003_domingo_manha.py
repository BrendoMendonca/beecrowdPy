def calcula_atraso(tempo):
    hora, min = map(int, tempo.split(':'))
    conversao = hora * 60 + min
    atraso = 8*60 - conversao
    return atraso
    
while True:
    try:
        hora = input()
        if(int(hora[0]) <= 7):
            atraso = 0
        else:
            atraso = 60 - calcula_atraso(hora)

        print(f"Atraso maximo: {atraso}")
    except EOFError:
        break