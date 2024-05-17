n = int(input())#recebimento da qunatidade de casos teste
for i in range(n):
    nome_escolha = input().split()#entrada dos nomes e das escolhads de jogada
    valor1, valor2 = map(int, input().split())#recebimento dos valores
    soma = valor1 + valor2#soma dos valores
    if(soma % 2 == 0):#verifica se é par ou impar
        if(nome_escolha[1] == 'PAR'):#verifica qual jogador escolheu par
            print(nome_escolha[1-1])
        else:
            print(nome_escolha[1+1])
    else:
        if(nome_escolha[1] == 'IMPAR'):#verifica qual jogador escolheu impar
            print(nome_escolha[1-1])
        else:
            print(nome_escolha[1+1])