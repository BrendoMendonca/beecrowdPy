caso = 0
while(True):
    try:
        n1 = int(input())
        n2 = int(input())
        n1 = str(n1)
        n2 = str(n2)
        tam_n1 = len(n1)
        caso += 1
        qnt_sub = 0
        for i in range(0, len(n2)):
            if(n2[i] == n1[0]):
                sequencia = []
                for j in range(i, len(n1), tam_n1):
                    sequencia.append(n2[j:j+tam_n1-1])
                if(sequencia[0] == n1):
                    qnt_sub += 1
                    posicao = i+1
        
        if(qnt_sub !=0):
            print(f"Caso: #{caso}")
            print(f"Qtd. Subsequencias: {qnt_sub}")
            print(f"Pos: {posicao}")
        else:
            print(f"Caso: #{caso}")
            print("Nao existe subsequencia")
        print(sequencia)
                    
    except EOFError:
        break