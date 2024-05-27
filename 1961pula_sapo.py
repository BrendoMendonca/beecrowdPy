alt_pulo, qnt_cano = map(int, input().split())#recebimento da altura que o sapo pula e da quantidade de canos
n_cano = list(map(int, input().split()))#entrada das alturas de cada cano
ant = n_cano[0]#variável que recebe a altura anterior da lista de altura dos canos
maior = False#variável que recebe verdade se a altura dos canos for maior do que a altura do pulo do sapo ou falso caso contrário
for i in range(1, qnt_cano):#laço de repetição para verificar a diferença de altura de cada cano
    if (abs(ant - n_cano[i]) > alt_pulo):#se a diferença de altura dos canos for maior do que o sapo pula, o valor lógico se torna true
        maior = True
    ant = n_cano[i]#incremento do valor anterior
#exibição do resultado
if(maior == True):
    print("GAME OVER")
else:
    print("YOU WIN")