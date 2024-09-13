import re
c, n = map(int, input().split())#recebimento do tamanho das cifras e da quantidade de frases

#recebimento das cifras
cifra_1 = input()
cifra_2 = input()


for _ in range(n):#recebimento das sentenças
    sentenca = input().upper()
    
    for caractere in sentenca:
        for indice, (c1, c2) in enumerate (zip(cifra_1, cifra_2)):
            if caractere == c2:
                sentenca = sentenca.replace(caractere, cifra_1[indice])
            if caractere == c1:
                sentenca = sentenca.replace(caractere, cifra_2[indice])
                

    print(sentenca)