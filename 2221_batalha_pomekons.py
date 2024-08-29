n = int(input())#recebimento da quantidade de testes

for i in range(n):#estrutura de repetição para recebimento dos tests
    
    bonus = int(input())#recebimento do valor do bonus
    #recebimento dos valores de ataque, defesa e level de cada jogador
    ataque_1, defesa_1, level_1 = map(int, input().split())
    ataque_2, defesa_2, level_2 = map(int, input().split())
    #calculo da força do golpe de cada jogador
    golpe_1 = (ataque_1+defesa_1)/2
    golpe_2 = (ataque_2+defesa_2)/2
    #verifica se os jogadorer receberão o bônus
    if(level_1 % 2 == 0):
        golpe_1 += bonus
        
    if(level_2 % 2 == 0):
        golpe_2 += bonus
    #verifica quem ganhou
    if(golpe_1 > golpe_2):
        print("Dabriel")
    elif(golpe_2 > golpe_1):
        print("Guarte")
    else:
        print("Empate")