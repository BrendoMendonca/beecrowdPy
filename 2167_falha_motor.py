n = int(input())#Recebimento da quantidade de velocidades
velocidades = list(map(int, input().split()))#recebimento das velocidades em uma lista
menor = velocidades[0]#inicialmente a menor velocidade é a primeira recebida
reducao = False#variável para determinar se houve a redução
for i in range(n):#estrutura de repetição para percorrer a lista e verificar as velocidas
    if(velocidades[i] < menor):#verifica se há redução
        queda = i + 1
        reducao = True
        break
    menor = velocidades[i]#atualização do valor da menor valocidade em cada ciclo
#exibição do resultado
if(reducao == True):
    print(queda)
else:
    print(0)