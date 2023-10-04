n = int(input()) #variável para a quantidade de casos

total = sapos = ratos = coelhos = 0 #inicialização do contador de cada cobaia e o total de cobaias

for i in range(n): #estrutura de repetição com n repetições para receber e calcular a quantidade de cada cobia
    tipo = input().split() #recebimento da quantidade e tipo de cobaia
    quant_tipo = int(tipo[0]) #variável que armazena a quantidade
    tipo = tipo[1] #armazenamento do tipo de cobaia
    total += quant_tipo #incremento do total
    #estrutura condicional para verificar o tipo de cobaia e incrementar a quantidade de cada
    if(tipo == 'S'):
        sapos += quant_tipo
    elif(tipo == 'R'):
        ratos += quant_tipo
    else:
        coelhos += quant_tipo

#exibição dos resultados
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")

print(f"Percentual de coelhos: {(coelhos/total)*100:.2f} %")
print(f"Percentual de ratos: {(ratos/total)*100:.2f} %")
print(f"Percentual de sapos: {(sapos/total)*100:.2f} %")