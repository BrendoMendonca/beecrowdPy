num_abas, num_acoes = map(int, input().split()) #recebimento da número de abas abertas inicialmente e a quantidade de ações que seram realizadas
for i in range(num_acoes):#estrutura de repetição para ajustar a quantidade de abas abertas
    acao = input()#recebimento da ação(fechou/clicou)
    #verifica a ação e incrementa ou decrementa de acordo com a entrada da ação
    if(acao == 'fechou'):
        num_abas += 1
    else:
        num_abas -= 1
#exibição do resultado        
print(num_abas)