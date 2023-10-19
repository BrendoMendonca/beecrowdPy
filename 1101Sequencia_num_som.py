while True:
    valores = input() #recebimento dos valores
    m, n = map(int, valores.split()) #atribuição dos valores para as varáveis
    soma = 0 #a soma em cada repetição é zerada
    if(m <= 0 or n <= 0): #verfica se os valores são menores ou iguais a zero(condiçãop de parada do laço de repetição)
        break
    if(m > n): #verifica qual valor é maior para atribuir às variáveis maior e menor
        maior = m
        menor = n
    else:
        maior = n
        menor = m

    for i in range (menor, maior + 1): #laço de repetição para exibir a sequencia de valores e calcular a soma
        print(f"{i} ", end='')
        soma += i
    print(f"Sum={soma}")