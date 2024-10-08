while True:
    try:
        n, id = map(int, input().split())#recebimento da quantidade de gameplays e do id
        cont = 0
        #recebimento e verificação das gameplays
        for _ in range(n):
            gameplay, cod = map(int, input().split())
            if(gameplay == id and cod == 0):
                cont+=1#incremento da quantiadde de gameplays de CS
        print(cont)                         
    except EOFError:
        break