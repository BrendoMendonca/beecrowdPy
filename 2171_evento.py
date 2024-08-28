while(True):#estrutura de repetição para recebimendo dos testes
    aumento, exp = map(int, input().split())#recebimento dos valores de aumento e exp
    if(aumento != 0 and exp != 0):#verifica se os valores recebidos são diferentes de 0
        print(f"{aumento * exp}")#exibição do resultado
    else:
        break