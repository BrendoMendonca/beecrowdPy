import sys
sys.setrecursionlimit(200000)
def merge_sort_custo(pecas):
    #caso base
    if len(pecas) == 1:
        return pecas, 0
    
    meio = len(pecas) // 2
    esquerda, custo_esq = merge_sort_custo(pecas[:meio])#chamada recursiva da função, usando o lado esquerdo da lista
    direita, custo_dir = merge_sort_custo(pecas[meio:])#chamada recursiva da função, usando o lado direito da lista
    
    ordenada, custo_merge = merge(esquerda, direita)
    return ordenada, custo_esq + custo_dir + custo_merge

def merge(esquerda, direita):
    resultado = []
    i = j = custo = 0
    
    soma_tempos_esq = sum(p[1] for p in esquerda)
    #somatório dos tempos da esquerda para calcular o custo de deslocamento
    while i < len(esquerda) and j < len(direita):
        #se a peça da esquerda for menor ou igual, não há troca de posição
        if esquerda[i][0] <= direita[j][0]:
            resultado.append(esquerda[i])
            soma_tempos_esq -= esquerda[i][1] #remove o tempo da soma conforme avança
            i += 1
        else:
            #se a peça da direita for menor, ela pula todos os elementos restantes da esquerda
            resultado.append(direita[j])
            #calcula o custo de tempo das trocas
            quantidade_pulada = len(esquerda) - i
            custo += soma_tempos_esq + (direita[j][1] * quantidade_pulada)
            j += 1
            
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado, custo

input_data = sys.stdin.read().split()#recebimento dos dados de entrada
idx = 0 #variável auxiliar para saber os dados que estão sendo tratados
while idx < len(input_data):
    try:
        n = int(input_data[idx])
        idx += 1
        val_pecas = list(map(int, input_data[idx:idx+n]))
        idx += n
        val_tempos = list(map(int, input_data[idx:idx+n]))
        idx += n
        
        #ordenação das listas que armazenam as peças e o tempo de ordenação
        pecas_com_tempo = list(zip(val_pecas, val_tempos))
        
        #como queremos apenas o custo do tempo, iremos usar apenas os valores do tempo e ignorar o valor das peças usando "_"
        _, custo_total = merge_sort_custo(pecas_com_tempo)
        print(custo_total)
    except:
        break