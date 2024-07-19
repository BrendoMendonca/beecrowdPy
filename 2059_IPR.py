#recebimento dos dados
escolha, player1, player2, roubo, acusa = map(int, input().split())

#verifica se o resultado da soma é par ou impar
if((player1 + player2) % 2 == 0):
    resultado = 1
else:
    resultado = 0

#caso o jogador 1 tenha roubado e o jogador 2 acusado
if(roubo == 1 and acusa == 1):
    print("Jogador 2 ganha!")

#caso o jogador 1 tenha roubado e o jogador 2 não tenha acusado
elif(roubo == 1 and acusa == 0):
    print("Jogador 1 ganha!")

#caso o jogador 1 não tenha roubado e o jogador 2 acusado    
elif(roubo == 0 and acusa == 1):
    print("Jogador 1 ganha!")
    
#caso o jogador 1 não tenha roubado e o jogador 2 não tenha acusado    
elif(roubo == 0 and acusa == 0):
    if(escolha == resultado):
        print("Jogador 1 ganha!")
    else:
        print("Jogador 2 ganha!")