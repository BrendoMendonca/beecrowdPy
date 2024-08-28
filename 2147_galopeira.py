n = int(input())#recebimento da quantidade de testes
for i in range(n):#estrutura de repetição para recebimento dos testes
    galope = input()#recebe a string
    tempo = len(galope)/100#calcula o tempo
    print(f"{tempo:.2f}")#imprime o resultado