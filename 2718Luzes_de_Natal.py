import re
n = int(input())#recebe a quantidade de grupos
for _ in range(n):
    valor = int(input())#recebe o número de piscas do grupo
    binario = bin(valor)[2:]#converte o valor para binário eliminando o "0b" do método
    sequencias = re.findall(r"1+", binario)#recebe as sequencias de "1" que há no grupo
    if sequencias:#verifica se há sequencia
        maior_sequencia = max(sequencias, key=len)#pega a maior sequencia de "1s"
        print(len(maior_sequencia))
    else:
        print(0)#exibe 0 caso não tenha "1" no grupo