N = int(input())#leitura da quantidade de pessoas
T = list(map(int, input().split()))#lista de quantas vezes Theon será atingido se ele escolher cada pessoa


min = min(T)#menor valor da listga
min_index = T.index(min)#indice do menor valor da lista

#impressão da posição do valor
print(min_index + 1)
