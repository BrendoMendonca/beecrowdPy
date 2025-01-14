import re
n = int(input())#recebimento da quantidade de casos teste
formato = r"^[A-Z]{3}-\d{4}$" #define o formato padrão das placas

for _ in range(n):
    placa = input()#recebimento da placa
    
    if(re.match(formato,placa)):#verifica se a placa está de acordo com o formato padrão
    #exibe o resultado de acordo com a numeração final da placa ou exibe a mensagem de erro
        if int(placa[-1]) == 1 or int(placa[-1]) == 2:
            print("MONDAY")
            
        elif int(placa[-1]) == 3 or int(placa[-1]) == 4:
            print("TUESDAY")
            
        elif int(placa[-1]) == 5 or int(placa[-1]) == 6:
            print("WEDNESDAY")
        
        elif int(placa[-1]) == 7 or int(placa[-1]) == 8:
            print("THURSDAY")
        
        elif int(placa[-1]) ==9 or int(placa[-1]) == 0:
            print("FRIDAY")
    else:
        print("FAILURE")