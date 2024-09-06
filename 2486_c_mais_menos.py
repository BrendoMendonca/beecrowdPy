while(True):#estrutura de repetição para recebimento dos casos
    
    total = 0#inicialmente o total de vitamina é 0
    qnt_alimento = int(input())#recebe a quantidade de alimentos
    
    if(qnt_alimento == 0):#verifica se a quantidade de alimentos é 0(condição de parada)
        break
    for _ in range(qnt_alimento):#estrutura de repetição para recebimento do alimento e quantidade de vitamnina
        
        entrada = input().split(maxsplit=1)#recebimento da quantidade e o alimnento
        #tratamento para separar a quantidade do alimento inserido na entrada
        quantidade = int(entrada[0])
        fruta = entrada[1]
        
        #verificação do alimento digitado e calculo da quantidade de vitamina consumida
        if(fruta == 'suco de laranja'):
            total += quantidade*120
            
        elif(fruta == 'morango fresco'):
            total += quantidade*85
        
        elif(fruta == 'mamao'):
            total += quantidade*85
        
        elif(fruta == 'goiaba vermelha'):
            total += quantidade*70
            
        elif(fruta == 'manga'):
            total += quantidade*56
            
        elif(fruta == 'laranja'):
            total += quantidade*50
            
        elif(fruta == 'brocolis'):
            total += quantidade*34
    
    #exibição dos resultados        
    if(total >= 130):
        print(f"Menos {total-130} mg")
    elif(total <= 110):
        print(f"Mais {110-total} mg")
    else:
        print(f"{total} mg")