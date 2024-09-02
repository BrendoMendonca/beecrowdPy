n = int(input())#recebimento da quantidade de competidores
for _ in range(n):#estrura de repetição para recebimento das notas
    nome = input()#recebimento do nome
    dificuldade = float(input())#recebimento do nível de dificuldade
    notas = list(map(float, input().split()))#recebimento das notas
    #remoção da maior e menor nota
    notas.remove(max(notas))
    notas.remove(min(notas))
    resultado = sum(notas) * dificuldade#calculo do resultado
    print(f"{nome} {resultado:.2f}")#exibição do resultado