import sys

def ordena_pecas(pecas):
    
    meio = len(pecas) // 2
    #chamada recursiva da função de ordenação para maximizar o tempo de busca e ordenação
    esquerda, custo_esq = ordena_pecas(pecas[:meio])#faz a busca do lado esquerdo do array
    direita, custo_dir = ordena_pecas(pecas[meio:])#faz a busca do lado direito do array
    
    ordenada, custo_merge = merge(esquerda, direita)
    return ordenada, custo_esq + custo_dir + custo_merge

def merge(esquerda, direita):
    resultado = []
    i = j = custo = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if pecas[j] > pecas[j+1]:
                pecas[j], pecas[j + 1] = pecas[j + 1], pecas[j]#realiza a troca
                tempo[j], tempo[j + 1] = tempo[j + 1], tempo[j]#calcula o tempo de troca
                custo += tempo[j] + tempo[j+1]
                """A linha de cima é equivalente a:
                aux = pecas[j]
                pecas[j] = pecas[j+1]
                pecas[j+1] = aux"""
    return custo
     
while True:
    try:
        n= int(input())
        pecas = list(map(int, input().split()))
        tempo = list(map(int, input().split()))
        print(ordena_pecas(pecas, tempo, n))
    except EOFError:
            break