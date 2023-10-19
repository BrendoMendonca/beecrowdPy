n = int(input()) #quantidade de casos teste

for i in range(n):#laço de repetição para receber os valores em cada caso teste
    valores = input() #recebimento de valores
    x, y = map(int, valores.split()) #atribuição dos valores para as varáveis
    soma = 0 #a soma em cada repetição é zerada

    if(x == y): #verifica se os valores são e exibe 0 caso for
        print(0)
    else:
        if(x>y): #verifica qual valor é maior para atribuir às variáveis maior e menor
            maior = x
            menor = y
        else:
            maior = y
            menor = x

        for j in range(menor + 1, maior): #laço de repetição que vai do menor valor +1 até o maior valor -1
            if(j % 2 != 0): #verifica se o valor de j é impar
                soma += j #caso j seja ímpar, o valor de j é incrementado na soma
        print(soma) #exibe a soma