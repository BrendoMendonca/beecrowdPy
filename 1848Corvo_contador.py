sorteio = [0, 0, 0] # lista para armazenar os números sorteados
num = 0

for i in range(3): #laço de repetição para recebimento dos 3 valores
    while True:#laço de repetição para soma do número "i"
        corvo = input()#recebimento do tipo de piscada
        if corvo == "caw caw":
            sorteio[i] = num
            num = 0
            break
        #incremento do número de acordo com o tipo de piscada
        elif corvo == "--*":
            num += 1
        elif corvo == "-*-":
            num += 2
        elif corvo == "-**":
            num += 3
        elif corvo == "*--":
            num += 4
        elif corvo == "*-*":
            num += 5
        elif corvo == "**-":
            num += 6
        elif corvo == "***":
            num += 7

#exibição dos valores
for num in sorteio:
    print(num)
