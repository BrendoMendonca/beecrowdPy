nao_atendido = 0 #inicialmente a quantidade de não atendidos é zero
#recebimento da quantidade de cada opção
opcoes = input()
opcao1, opcao2, opcao3 = map(int, opcoes.split())

#recebimento da quantidade de pedido de cada opção
pratos = input()
frango, bife, massa = map(int,  pratos.split())

#verifica a quantidade de passageiros não atendidos
if(opcao1 < frango):
    nao_atendido += frango-opcao1
if(opcao2 < bife):
    nao_atendido += bife-opcao2
if(opcao3 < massa):
    nao_atendido += massa-opcao3
#exibe a quantidade de passageiros não atendidos
print(nao_atendido)