import re
c, n = map(int, input().split())

cifra_1 = input()
cifra_2 = input()

for _ in range(n):
    sentenca = input().upper()
    
    for caractere in sentenca:
        for indice, c in enumerate(cifra_1):
            if caractere == c:
                caractere = cifra_2[indice]

    print(sentenca)