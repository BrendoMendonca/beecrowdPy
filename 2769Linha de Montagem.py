import sys
while True:
    try:
        
        n = input()
        n = int(n)
        tempo = 0
        linha1 = False
        e1, e2 = map(int, input().split())
        
        tempo += min(e1, e2)
        
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
                    
        trocaA_B = list(map(int, input().split()))
        trocaB_A = list(map(int, input().split()))

        x1, x2 = map(int, input().split())

        f1 = [0] * n
        f2 = [0] * n
        
        # Caso base: primeira estação
        f1[0] = e1 + a1[0]
        f2[0] = e2 + a2[0]
        
        # Preenchimento da tabela DP
        for i in range(1, n):
            # Para chegar na estação i da linha 1:
            # Vem da linha 1 anterior OU vem da linha 2 anterior + troca
            f1[i] = min(f1[i-1] + a1[i], f2[i-1] + t2[i-1] + a1[i])
            
            # Para chegar na estação i da linha 2:
            # Vem da linha 2 anterior OU vem da linha 1 anterior + troca
            f2[i] = min(f2[i-1] + a2[i], f1[i-1] + t1[i-1] + a2[i])
        
        # Resultado final considerando a saída x
        resultado = min(f1[n-1] + x1, f2[n-1] + x2)
        print(resultado)
        
        """if(e1 == e2):
            if (e1+a1[0]) < (e2+a2[0]):
                linha1 = True
        else:
            if e1 < e2:
                linha1 = True       

        for i in range(int(n)-1):
            if linha1:
                menor_caminho = min(a1[i], (trocaA_B[i] + a2[i]))
            else:
                menor_caminho = min(a2[i], (trocaB_A[i] + a1[i]))
            tempo += menor_caminho
        
        if linha1:
            tempo += x1
        else:
            tempo += x2
        
        print(tempo)"""

    except EOFError:
        break