while(True):#estrutura de repetição para recebimento dos casos
    valor, pag = map(int,input().split())#recebimento do valor da compra e do pagamento
    if(valor == pag):#verifica a condição de parada
        break
    notas = [2, 5, 10, 20, 50, 100] #lista com as notas disponíveis para troco
    troco = pag - valor #calculo do valor do troco
    tem_troco = False #inicialmente o valor lógico para "tem_troco" é falso
    
    #estruturas de repetição para calcular a soma de todas as cédulas disponíveis de dois em dois
    for i in range(len(notas)):
        for j in range(len(notas)):
            if(notas[i] + notas[j] == troco):#verifica se é possível dar troco
                tem_troco = True#mudança do valor lógido de "tem_troco" para true
                break
            
         #impressão do resultado   
        if tem_troco == True:
            print("possible")
            break
        
    if(tem_troco == False):
        print("impossible")    