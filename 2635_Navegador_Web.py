while(True):
    try:
        palavras_pesquisadas = []#lista que armazena as palavras pesquisadas
        
        num_palavras = int(input())#recebe a quantidade de palavras pesquisadas
        for _ in range(num_palavras):#recebimento das palavras
            pesquisa = input()
            palavras_pesquisadas.append(pesquisa)
    
        num_consultas = int(input())#recebe a quantidade de consultas
        for _ in range(num_consultas):
            sugestao = 0
            maior_palavra = 0
            busca = input() #recebe as strings consultadas
            
            for i in range(num_palavras):
                if(busca == palavras_pesquisadas[i][:len(busca)]):#verifica se a consulta faz parte de alguma palavra já pesquisada anteriormente
                    sugestao +=1 #faz o incremento na quantidade de sugestões
                    if(len(palavras_pesquisadas[i]) > maior_palavra):#verifica a maior palavra que faz parte das consultas
                        maior_palavra = len(palavras_pesquisadas[i])
#exibição dos resultados                        
            if(sugestao == 0):
                print(-1)
            else:
                print(f"{sugestao} {maior_palavra}")    
    except EOFError:
        break