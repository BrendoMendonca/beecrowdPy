while(True):
    try:
        quant_lesma = int(input())#recebe a quantidade de lesmas
        lesmas = []#lista que armazenará as velocidades do grupo
        lesmas = list(map(int, input().split())) #recebimento das velocidades
        maior = max(lesmas, key=int)#maior velocidade da lista
        #verifica em qual categoria a maior velocidade se encontra
        if(maior < 10):
            print(1)
        elif(maior >= 20):
            print(3)
        else:
            print(2)

    except EOFError:
        break