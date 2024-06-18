n = int(input())#recebe a quantidade de sítios que podem ser visitados
sitio = list(map(int, input().split()))#recebimento da quantidade de carneiros em cada sítio
index = total = 0#index e o total de carneiros iniciamente são 0
visitado = set()#variável para marcar os sítios visitados

while 0 <= index < len(sitio):#estrutura de repetição para percorrer a lista até chegar em um sítio com 0 carneiros ou até visitar todos os sítios
    
    valor_ant = sitio[index]#armazena o valor atual da quantidade de carneiros no sítio "i"
    
    if(valor_ant != 0):#verifica se tem carneiro no sítio        
        sitio[index]-=1#decremente a quantidade de carneiros do sítio
    
    visitado.add(index)#marca o sítio como visitado
    
    #verifica se o valor da quantidade de carneiros é par ou ímpar para decidir qual o próximo sítio visitado
    if(valor_ant % 2 != 0):
        index+=1
    else:
        index-=1

#calcula a quantidade de carneiros restantes
for carneiro in sitio:
    total += carneiro       

print(f"{len(visitado)} {total}")#exibição dos resultados