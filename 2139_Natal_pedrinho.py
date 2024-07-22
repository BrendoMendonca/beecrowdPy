from datetime import date #importação da biblioteca daterime para calcular os dias restantes para o natal
while(True):#laço de repetição para recebimento dos casos
    try:
        mes, dia = map(int, input().split())#recebimento do mês e dia
        if (mes == 12):#verifica se o mês digitado é o do natal
            #verificações do dia dentro do mês do natal
            if(dia == 24):
                print("E vespera de natal!")
            elif(dia == 25):
                print("E natal!")
            elif(dia > 25):
                print("Ja passou!")
        else:
            dias = date(2016, 12, 25) - date(2016, mes, dia)#calculo da quantidade de dias restantes para o natal
            print(f"Faltam {dias.days} dias para o natal!")
    except EOFError:
        break