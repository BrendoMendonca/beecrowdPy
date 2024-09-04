while(True):#estrutura de repetição para recebimento dos casos
    patinhos = int(input())#recebimento da quantidade inicial de patinhos
    if patinhos == -1:#verifica se a entrada nao foi a condição de parada -1
        break
    elif patinhos != 0:#verifica se  a entrada é diferente de 0 e faz o decremento de -1
        patinhos -=1
    print(patinhos)#exibição do resultado
    