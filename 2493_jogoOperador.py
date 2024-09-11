def calculo(operador1, operador2, operacao):#função que verifica a operação a ser realizada e retorna o valor calculado
    if(operacao == '+'):
        return operador1 + operador2
    
    elif(operacao == '-'):
        return operador1 - operador2
    
    elif(operacao == '*'):
        return operador1 * operador2

while(True):#estruta de repetição para recibmento dos casos
    try:
        
        qnt = int(input())#recebimento da quantidade de jogadores
        #listas para armazenamento das expressoes, resultados, informações dos jogadores e os jogadores eliminados
        expressoes = []
        resultado = []
        jogadores = []
        eliminados = []
        
        for _ in range(qnt):#recebimento das expressoes            
            expressoes.append(input())        
                  
        for exp in expressoes:#estrutura de repetição para tratamento das expressoes
            valores = exp.replace('=', ' ').split()#recebimento dos valores da expressão separados em uma lista
            #alocação do valor dos operadores e do resultado esperado da expressao
            operador1 = int(valores[0])
            operador2 = int(valores[1])
            resultado_correto = int(valores[2])
            resultado.append((operador1, operador2, resultado_correto))#armazenamento dos valores na lista de resultados
                
        for _ in range(qnt):#estrutura de repetição para recebimento da entrada dos jogadores(nome, indice da operação e operador)
            jogador = input().split()
            jogadores.append(jogador)

        #atribuição das entradas dos jogadores às variáveis
        for jogador in jogadores:
            nome = jogador[0]
            indice = int(jogador[1]) - 1
            operacao = jogador[2]

            operador1, operador2, resultado_correto = resultado[indice]#atribuição dos operadores e do resultado correto

            
            if operacao == 'I':#verifica se o jogador escolheu a opção "impossível" e verifica se ele está correto
                if (
                    calculo(operador1, operador2, '+') != resultado_correto and
                    calculo(operador1, operador2, '-') != resultado_correto and
                    calculo(operador1, operador2, '*') != resultado_correto
                ):
                    continue  #resposta Impossível está correta
                else:
                    eliminados.append(nome)#incremento na lista de eliminados, caso o jogador esteja errado
            else:
                resultado_jogador = calculo(operador1, operador2, operacao)# cálculo do resultado de acordo com a operação escolhida
                if resultado_jogador != resultado_correto:#verifica se o resultado está errado com base na operação
                    eliminados.append(nome)#incremento na lista de eliminado

        #impressão dos resultados
        if len(eliminados) == 0:
            print("You Shall All Pass!")
        elif len(eliminados) == qnt:
            print("None Shall Pass!")
        else:
            eliminados.sort()
            print(" ".join(eliminados))
                
        
    except EOFError:
        break