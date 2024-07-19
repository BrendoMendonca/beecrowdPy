caso = 0 #inicialmente a quantidade de casos é zero
while(True):#estrutura de repetição para recebimento dos casos
    try:
        #recebimento dos valores
        n1 = input()
        n2 = input()
        tam_n1 = len(n1)#armazena o tamanho de n1
        caso += 1 #incremento do valor da quantidade de casos
        qnt_sub = 0#variável que armazena a quantidade de cada subsequencia
        for i in range(0, len(n2)):#estrutura de repetição para verificar se há subsequencia
            if(n2[i] == n1[0]):#verifica se os algarismos  da sequencia(n2) são iguais primeiro algarismo do número(n1)
                if n2[i:i+tam_n1] == n1:#verifica se a sequência(n2) de i até i + tamanho de n1 é igual a n1
                    qnt_sub += 1#incremento na quantidade de subsequencia
                    posicao = i+1#incremento na posição da sequencia
                    
        #impressões dos resultados
        print(f"Caso #{caso}:")
        
        if(qnt_sub != 0):
            print(f"Qtd.Subsequencias: {qnt_sub}")
            print(f"Pos: {posicao}\n")
        else:
            print("Nao existe subsequencia\n")
                   
    except EOFError:
        break