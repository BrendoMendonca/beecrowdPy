n = int(input())#recebimento da quantidade de casos testes

for i in range(n):#estrutura de repetição para recebiemnto dos casos
    hora, min, porta = map(int, input().split())#recebimento das entradas
    #verifica se a porta abriu ou fechou e faz a impressão do resultado devidamente formatado
    if(porta == 1):
        print(f"{hora:02}:{min:02} - A porta abriu!")
    else:
        print(f"{hora:02}:{min:02} - A porta fechou!")