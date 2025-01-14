import sys
def primo(valor):#método que verifica se o número é primo
    if valor == 1:
        return -1
    div = 0
    for i in range(1, valor+1):
        if valor % i == 0:
            div += 1
    if div > 2:
        return -1
    
    return 0        

for linha in sys.stdin:#recebimento da quantidade de moedas em cada caso
    try:
        qnt_moedas = int(linha)
        moedas = []#lista para armazenar os valores das moedas
        soma = 0
        for _ in range(qnt_moedas):#recebimento dos valores das moedas
            valor = int(input())
            moedas.append(valor)
            
        salto = int(input())#recebimento do valor do salto
        
        for valores in moedas[::-salto]:#faz a soma dos valores das moedas 
            soma += valores
        
        resultado = primo(soma)#chama a função primo() para verificar se o núemro é primo
        #imprime o resultado
        if(resultado == 0):
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I’ll hit you.")    
        
    except EOFError:
        break