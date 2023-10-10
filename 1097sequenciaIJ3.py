j = 7
for i in range(1, 10, 2):#estrutura de repetição para incrementar o "i"
    aux_j = j + 2 #variável que atualiza o valor de "j"
    for cont in range(3): #o "i" e o "j" são impressos 3 vezes
        print(f"I={i} J={j}")
        j -= 1 #decremento de "j"
    j = aux_j #"j" recebe seu valor original + 2