n = float(input())#recebimento do valor
notacao = format(n, ".4e")#conversão do float para notação científica
if n > 0 or notacao[0] == '0':#verifica se o valor é igual ou maior que 0 para adicionar o "+" no início
    print("+", end="")

print(notacao.upper())#exibe o resultado