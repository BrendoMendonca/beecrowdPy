valor = int(input())#recebimento do valor
valor = str(valor)#transformação do valor em str para resolver problemas de quebra de linha
tamanho = len(valor)#tamano armazena o tamanho da quantidade de números
for i in range(tamanho-1, -1, -1):#estrutura de repetição para percorrer os númerops de tras para frente
    print(valor[i], end="")#exibição do número invertido
    
print()