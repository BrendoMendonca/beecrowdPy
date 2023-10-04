numeros = [] #lista onde os números serão armazenados
maior = 0 #variável que será armzenado  maior numero
for i in range(1, 101): #estrutura de repetição para receber os npumeros
    numeros.append(int(input())) #entrada dos números na lista
    if numeros[i-1] > maior: #verifica se o número adicionado é maior que a variável "maior"
        maior = numeros[i-1] #se for maior, a variável recebe  valor inserido
        maior_posi = i #veriável que armazena a posição do maior número

print(maior)
print(maior_posi)