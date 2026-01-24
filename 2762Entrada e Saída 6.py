while(True):
    try:
        valor = input().split('.',1)
        parte1 = valor[0]
        parte2 = valor[1].lstrip('0')#garante a remoção do 0 à esquerda da parte decimal
        print(parte2, end='.')
        print(parte1)
    except EOFError:
        break