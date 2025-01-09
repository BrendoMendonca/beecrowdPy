qnt_comp = int(input())#recebimento da quantidade de competidores
qnt_vagas = int(input())#quantidade mínima de vagas
classificados = qnt_vagas#quantidade de classificados inicial
pontuacao = []#lista para armazenas as pontuações

for _ in range(qnt_comp):#recebimento das pontuações
    pontuacao.append(int(input()))
  
pontuacao = sorted(pontuacao, reverse=True)#ordena as pontuações do maior para o menor
for i in range(qnt_vagas, qnt_comp):#verifica se as pontuações a partir da quantidade de vagas são iguais
    if(pontuacao[qnt_vagas-1] == pontuacao[i]):
        classificados += 1#se for igual a quantidade de classificados aumenta
print(classificados)#exibe o resultado