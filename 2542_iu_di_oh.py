while True:
    try:
        n = int(input())#recebimento da quantidade de atributos das cartas
        marcos, leo = map(int, input().split())##recebimento da quantidade de baralhos de cada jogador
        baralho_m = []
        baralho_l = []
        
        #recebimento dos atributos das cartas de cada jogador
        for _ in range(marcos):
            baralho_m.append(list(map(int, input().split())))
            
        for _ in range(leo):
            baralho_l.append(list(map(int, input().split())))

        #recebimento da escolha da carta de cada jogador e o atributo que será disputado            
        escolha_marcos, escolha_leo = map(int, input().split())        
        sorteio = int(input()) -1
        
        #verifica e exibie o vencedor
        if baralho_m[escolha_marcos-1][sorteio] > baralho_l[escolha_leo-1][sorteio]:
            print("Marcos")
        elif baralho_m[escolha_marcos-1][sorteio] < baralho_l[escolha_leo-1][sorteio]:
            print("Leonardo")
        else:
            print("Empate")         
    except EOFError:
        break