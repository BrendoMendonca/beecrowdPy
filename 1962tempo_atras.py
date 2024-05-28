n = int(input())#recebimento da quantidade de anos
for i in range(n):#estrutura de repetição para receber os anos
    tempo = int(input())#recebimento dos anos
    #exibição dos resultados
    if(tempo >= 2015):
        print(f"{tempo - 2015 + 1} A.C.")
    else:
        print(f"{abs(tempo - 2015)} D.C.")