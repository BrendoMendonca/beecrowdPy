while True:
    try:
        n_jog = int(input())#recebimento da quantidade de jogadores
        votos = input().split()#recebimento dos votos de cada jogador
        resultado = votos.count("1")#contagem dos votos
        if(resultado >= 2/3*n_jog):#verifica o resultado dos votos e exibe na tela
            print("impeachment")
        else:
            print("acusacao arquivada")
    except EOFError:
        break