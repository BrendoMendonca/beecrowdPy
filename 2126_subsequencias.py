caso = 0 #inicialmente a quantidade de casos é zero
while(True):#estrutura de repetição para recebimento dos casos
    try:
        #recebimento dos valores
        n1 = input()
        n2 = input()
        tam_n1 = len(n1)#armazena o tamanho de n1
        caso += 1 #incremento do valor da quantidade de casos
        qnt_sub = 0#
        for i in range(0, len(n2)):
            if(n2[i] == n1[0]):
                if n2[i:i+tam_n1] == n1:
                    qnt_sub += 1
                    posicao = i+1
                    
        print(f"Caso #{caso}:")
        
        if(qnt_sub != 0):
            print(f"Qtd.Subsequencias: {qnt_sub}")
            print(f"Pos: {posicao}\n")
        else:
            print("Nao existe subsequencia\n")
                   
    except EOFError:
        break