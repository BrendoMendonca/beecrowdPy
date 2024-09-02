n = int(input())#recebimento da quantidade de jogares analisados
#inicialmente a quantidade de jogadas e jogadas de sucesso são 0
saques = bloqueios = ataques = 0
saque_suc = bloqueio_suc = ataque_suc = 0

for _ in range(n):#estrutura de repetição para recebimento dos valores
    nome = input()#recebimento do nome
    
    s, b, a = map(int, input().split())#recebimento da quantidade de jogadas do jogador
    #incremento do valor inicial das jogadas
    saques += s
    bloqueios += b
    ataques += a
    
    s_suc, b_suc, a_suc = map(int, input().split())#recebimento das jogadas de sucesso
    #incremento do valor inicial das jogadas de sucesso
    saque_suc += s_suc
    bloqueio_suc += b_suc
    ataque_suc += a_suc

#exibição dos resultados
print(f"Pontos de Saque: {saque_suc/saques*100:.2f} %.")
print(f"Pontos de Bloqueio: {bloqueio_suc/bloqueios*100:.2f} %.")
print(f"Pontos de Ataque: {ataque_suc/ataques*100:.2f} %.")