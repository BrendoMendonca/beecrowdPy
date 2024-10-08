while True:
    try:
        n_hab, n_cons = map(int, input().split())#recebimento do número de habitantes e do número de coinsultas
        notas = []
        for i in range(n_hab):
            notas.append(int(input()))#recebimento das notas
        notas.sort(reverse=True)#ordena as notas da maior para a menor
        for _ in range(n_cons):
            consulta = int(input())#recebimento das consultas
            print(f"{notas[consulta-1]}")#exibição das consultas
    except EOFError:
        break