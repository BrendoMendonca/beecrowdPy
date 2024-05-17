n = int(input())#recebimento da qunatidade de casos teste
for i in range(n):#estrutura de repetição para recebimento das informações
    info = input().split()#recebimento do nome e força aplicada separando cada informação
    if(info[0] != 'Thor'):#verifica se é o thor que está levantando o martelo
        print('N')
    else:
        print('Y')