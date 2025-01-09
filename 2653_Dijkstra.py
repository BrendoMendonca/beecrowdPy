joias = []#lista para armazenar os caracteres que representam as joias
while True:
    try:
        joia = input()#recebimento das entradas
        if joia not in joias:#verifica se a joia já está na lista
            joias.append(joia)#se não estiver, a joia entra para a lista
    except EOFError:
        print(len(joias))#imprime o resultado
        break