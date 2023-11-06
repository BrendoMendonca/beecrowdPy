partidas = empate = vit_inter = vit_gremio = 0

while(True):
    gols = input()
    inter, gremio = map(int, gols.split())
    if(inter > gremio):
        vit_inter += 1
        resultado = "Inter venceu mais"

    elif(gremio > inter):
        vit_gremio += 1
        resultado = "Gremio venceu mais"

    else:
        empate += 1
        resultado = "Nao houve vencedor"

    partidas +=1

    print("Novo grenal (1-sim 2-nao)")
    nova_partida = int(input())
    if(nova_partida == 2):
        break

print(f"{partidas} grenais")
print(f"Inter:{vit_inter}")
print(f"Gremio:{vit_gremio}")
print(f"Empates:{empate}")
print(resultado)