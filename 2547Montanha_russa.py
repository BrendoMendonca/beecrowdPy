while True:
    try:
        #recebimento da quantidade de recebimentos de altura e a altura minima e maxima
        n, alt_min, alt_max = map(int, input().split())
        cont = 0#contador de alturas aptas
        for _ in range(n):
            altura = int(input())#recebimento das alturas
            if(altura >= alt_min and altura <= alt_max):#verifica se as alturas são aptas
                cont+=1#incremento do contador
        print(cont)#exibição do resultado
    except EOFError:
        break