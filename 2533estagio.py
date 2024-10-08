while True:
    try:
        nota = carga_hora = numerador = denominador = 0#inicialização das variáveis
        n = int(input())#recebimento da quantidade de disciplinas
        for i in range(n):#estrutura de repetição para recebimento das notas, carga horária e para o calculo do denominador e numerador da fórmula
            nota, carga_hora = map(int, input().split())
            numerador = nota*carga_hora + numerador
            denominador += carga_hora
            
        #cálculo e exibição do IRA
        ira = numerador/denominador
        print(f"{ira/100:.4f}")
            
    except EOFError:
        break