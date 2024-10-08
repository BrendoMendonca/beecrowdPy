from math import sqrt
while True:#estrutura de repetição para recebimento dos casos
    try:
        #recebimento da quantidade de linhas e colunas da cidade    
        linha, coluna = map(int, input().split())        

        for i in range(linha):#estrutura de repetição que percorre as linhas
            linha_cidade = input().split()#recebimento dos valores das linhas
            for j in range(coluna):#estrutura de repetição para percorrer as colunas
                valor = int(linha_cidade[j])#recebe o valor de cada coluna
                #verificação da coornedanda do analógimôn e do jogador
                if(valor == 2):
                    x1 = i + 1
                    y1 = j + 1
                elif(valor == 1):
                    x2 = i + 1
                    y2 = j + 1
        #calculo da distancia entre o analógimôn e o jogador                    
        distancia = abs(x2 - x1) + abs(y2 - y1)
        print(distancia)
        
    except EOFError:
        break