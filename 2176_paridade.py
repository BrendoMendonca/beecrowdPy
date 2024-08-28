valor_bin = list(map(int, input().strip()))#recebimento do valor binário e transforma em uma lista de int
qnt_1 = valor_bin.count(1)#conta quantos 1s tem no valor passado
#verifica a paridade de 1s
if(qnt_1 % 2 != 0):
    valor_bin.append(1)
else:
    valor_bin.append(0)

valor_bin = ''.join(map(str, valor_bin))#transforma o valor atualizado em uma string de números
print(valor_bin)#exibe o resultado