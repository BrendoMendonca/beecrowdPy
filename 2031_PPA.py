n = int(input())#recebimento da quantidade de casos teste
for i in range(n):#estrutura de repetição para realização dos casos teste
    #recebimento da jogada dos jogadores
    player1 = input()
    player2 = input()
    
    #verificação e exibição de cada caso
    if(player1 == player2):
        if(player1 == 'ataque'):
            print("Aniquilacao mutua")
        
        elif(player1 == 'pedra'):
            print("Sem ganhador")
        
        elif(player1 == 'papel'):
            print("Ambos venceram")
            
    else:
        if(player1 == 'ataque'):
            print("Jogador 1 venceu")
        elif(player2 == 'ataque'):
            print("Jogador 2 venceu")
        
        elif(player1 == 'pedra' and player2 == 'papel'):
            print("Jogador 1 venceu")
        else:
            print("Jogador 2 venceu")
                