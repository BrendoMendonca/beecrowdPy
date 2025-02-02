renas = ("Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen", "Rudolph")
bolas = list(map(int, input().split()))
total = sum(bolas)

i = (total - 1) % len(renas)
nome = renas[i]
print(nome)