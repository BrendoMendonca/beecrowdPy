while(True):
    try:
        c, n = map(int, input().split())#recebimento do tamanho das cifras e da quantidade de frases

        
        decifra = {}#dicionário para recebimento dos caracteres usados para decifrar as palavras
        
        #recebimento das cifras
        cifra_1 = input()
        cifra_2 = input()

        #cifras com letras minusculas
        lowerCifra_1 = cifra_1.lower()
        lowerCifra_2 = cifra_2.lower()

        #preenchimento do dicionário
        for i in range(c):
            #mapeamento dos caracteres da cifra 1 e da cifra 2
            decifra[cifra_1[i]] = cifra_2[i]#a chave 'cifra_1[i]' recebe o valor "cifra_2[i]"
            decifra[cifra_2[i]] = cifra_1[i]
            decifra[lowerCifra_1[i]] = lowerCifra_2[i]
            decifra[lowerCifra_2[i]] = lowerCifra_1[i]

        #recebimento das sentenças
        for _ in range(n):
            sentenca = input()
            for letra in sentenca:#verifica cada caractere da sentença e imprime de acordo com a tradução
                print(decifra.get(letra, letra), end='')#o método get() verifica se o caractere está no dicionário de decifra
            print('')
        print()
    except EOFError:
        break