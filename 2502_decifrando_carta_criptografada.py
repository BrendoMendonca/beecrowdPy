import re
c, n = map(int, input().split())

cifra_1 = input()
cifra_2 = input()

for _ in range(n):
    sentenca = input().upper
    
    for indice, caractere in enumerate(sentenca):
        for c in cifra_1:
            if caractere == c:
                caractere = cifra_2[indice]

    print(sentenca)