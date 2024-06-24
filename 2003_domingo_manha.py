def converte_tempo(tempo):#função que converte as horas em minutos
    hora, min = map(int, tempo.split(':'))#recebimento do tempo e convertendo os valores em inteiro
    conversao = hora * 60 + min#calculo da conversão de tempo para minutos
    return conversao#retorno do calculo
    

def calcula_atraso(tempo):#função que calcula o atraso 
    conversao = converte_tempo(tempo)#uso da função que converte o tempo
    atraso = 8*60 - conversao#calculo do valor do atraso
    return atraso#retorno do valor do atraso


while True:#estrutura de repetição para realização dos casos teste
    try:
        horario = input()#recebimento dos valores teste
        minutos = converte_tempo(horario)#minutos recebe o valor do tempo convertido em minutos
        if(minutos <= 420):#se o valor dos minutos for menor ou igual a 420, significa que não há atraso
            atraso = 0
        else:#caso contrário o calculo de atraso é realizado
            atraso = 60 - calcula_atraso(horario)

        print(f"Atraso maximo: {atraso}")#exibição do resultado
    except EOFError:
        break