while True:#laço de repetição para recebimento dos casos
    t = int(input()) #recebimento da quantidade de testes
    if(t == 0):#verifica a condição de parada 
        break
    for i in range(t):
        qnt_pessoas = int(input())#recebimento da quanitdade de pessoas
        #verifica se o valor de entrada é par ou impar e calcula a quantidade de pedidos
        if(qnt_pessoas % 2 != 0):
            pedidos = (qnt_pessoas - 1) * 2 + 1
        else:
            pedidos = (qnt_pessoas - 2) * 2 + 2
        #exibe o resultado
        print(pedidos)