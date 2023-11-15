soma = 0#inicialmente a soma é zero

valores = input().split()#recebimento dos valores iniciais como string

#as variaveis "a" e "n" armazenas os valores como inteiros
a = int(valores[0])
n =  int(valores[1])

if (n <= 0):#verifica se n é menor ou igual a zero para que outros valores sejam atribuídos para "n" até que o valor seja válido
    i = 2
    while(n<=0):
        n = int(valores[i])
        i+=1

for i in range(0, n):#cálculo da soma dos valores
    soma += i + a
print(soma)