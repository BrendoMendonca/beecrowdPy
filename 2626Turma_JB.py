while True:
    try:
        dodo, leo, pepper = input().split()#recebimento dos dados
        #verifica o vencedor e imprime suas frases de vitória        
        if (dodo == 'papel' and leo == 'pedra' and pepper == 'pedra' or
            dodo == "pedra" and leo == "tesoura" and pepper == "tesoura" or
            dodo == "tesoura" and leo == "papel" and pepper == "papel"):
                print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
                
        elif(leo == 'papel' and dodo == 'pedra' and pepper == 'pedra' or
            leo == "pedra" and dodo == "tesoura" and pepper == "tesoura" or
            leo == "tesoura" and dodo == "papel" and pepper == "papel"):
            print("Iron Maiden's gonna get you, no matter how far!")
            
        elif(pepper == 'papel' and leo == 'pedra' and dodo == 'pedra' or
            pepper == "pedra" and leo == "tesoura" and dodo == "tesoura" or
            pepper == "tesoura" and leo == "papel" and dodo == "papel"):
                print("Urano perdeu algo muito precioso...")
        else:#caso dê empate
            print("Putz vei, o Leo ta demorando muito pra jogar...")
            
    except EOFError:
        break