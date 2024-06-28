caso = 0#inicialmente o numero de casos é zero

while True:#estrutura de repetição para recebimento dos casos
    try:
        n = int(input())#recebimento do último número da sequência
        qnt_num = 0#a quantidade de números da sequencia inicialmente é zero em cada caso
        sequencia = [] #variável composta para armazenar a sequencia
        sequencia.append(0)#adiciona o valor zero à lista
        for i in range(n+1):#estrutura de repetição para adição dos valores à lista
            for j in range(i):#estrutura de repetição auxiliar para adiconar os valores repetidos
                sequencia.append(i)
        
        caso+=1#incremento do valor do número do caso
        
        if(len(sequencia) <= 1):#exibição do número do caso e da quantidade de números da sequência
            print(f"Caso {caso}: {len(sequencia)} numero")
        else:
            print(f"Caso {caso}: {len(sequencia)} numeros")
        
        ultimo = 1#variável que controla a verificação do último elemento da lista para exibição da maneira correta
        
        #exibição da sequencia  
        for i in sequencia:
            if(ultimo == len(sequencia)):
                print(i)
            else:
                print(i, end=' ')
            ultimo +=1
        print()        
    except EOFError:
        break