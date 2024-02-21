while True:
    valores = input().split()#recebimento dos valores
    if valores[0] == '0': #critério de parada
        break
    A, B, C = map(int, valores)#valçores convertidos para inteiro
    
    area_casa = A * B #cálculo da área da casa
    lado_terreno = int((area_casa / (C / 100)) ** 0.5) #cálculo da lateral da casa
    
    print(lado_terreno)#impressão do valor
