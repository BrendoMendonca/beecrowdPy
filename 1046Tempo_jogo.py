valores = input()
inicio, fim = map(int, valores.split())

if(inicio == fim):
    print("O JOGO DUROU 24 HORA(S)")
elif(inicio < fim):
    total = fim - inicio
    print(f"O JOGO DUROU {total} HORA(S)")
elif(fim < inicio):
    total = (24 - inicio) + (fim)
    print(f"O JOGO DUROU {total} HORA(S)")