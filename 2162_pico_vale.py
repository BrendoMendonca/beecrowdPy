n = int(input())#recebimento da quantidade de valores
valores = input()#recebimento das alturas
alturas = [int(num) for num in valores.split()]#alocando os valores das alturas em um array
paisagem = 0#inicialmente os valores não formam uma paisagem

if(n == 2):#verifica se a quantidade de alturas informada é 2 e faz um simples teste de paisagem
    if(alturas[0] != alturas[1]):#verifica se as alturas são diferentes e modifica o valor de paisagem
        paisagem = 1
#caso tenha mais de duas alturas
else:
    for i in range(len(alturas)-2):#estrutura de repetição para percorrer o array até o antipenultimo elemento
        paisagem = 0#a cada início de repetição a paisagem recebe o valor 0 para que seja atualizado a cada verificação
        if((alturas[i] < alturas[i+1] and alturas[i+1] > alturas[i+2])) or (alturas[i] > alturas[i+1] and alturas[i+1] < alturas[i+2]):#caso atenda os critérios de paisagem, o valor da paisagem é alterado para 1
            paisagem = 1
#impressão do valor da paisagem
print(paisagem)