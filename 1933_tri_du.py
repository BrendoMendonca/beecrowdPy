carta1, carta2 = map(int, input().split())
if (carta1 > carta2) or (carta1 == carta2):
    print(carta1)
else:
    print(carta2)