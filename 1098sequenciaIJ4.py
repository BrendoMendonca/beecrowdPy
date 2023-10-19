j = [1,2,3] #lista com os valores iniciais de j
i = 0
while(i<=1.8): #i e j serão impressos até i ser igual a 1.8
    for cont in range(3):
        if ((i>0 and i<1) or (i>1 and i<2)): #verifica se i não é inteiro
            print(f"I={i:.1f} J={j[cont]:.1f}")
        else:
            print(f"I={i:.0f} J={j[cont]:.0f}")
        j[cont] += 0.2
    i += 0.2
"""OBS
USANDO O MÉTODO ANTERIOR, NÃO CONSEGUI EXIBIR OS VALORES INTEIROS QUANDO I É MAIOR QUE 1.8
*MESMO COM A CONDIÇÃO DO WHILE AJUSTADA"""
#gambiarra para exibição dos 3 últimos resultados, quando i é maior que 1.8
a = 2
b = 3
for n in range(3):
    print(f"I={a} J={b}")
    b += 1