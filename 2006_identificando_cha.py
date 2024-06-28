tipo = input()#recebimento do valor do tipo de chá
respostas = input().split()#recebimento das respostas dos participantes
acertos = 0#variável que armazena a quantidade de acertos
for opcao in respostas:#estrutura de repetição para verificar cada resposta e incrementear a quantidade de acertos
    if(opcao == tipo):#verifica se a opção é a correta
        acertos += 1#incremento do acerto
    
print(acertos)#exibição do resultado