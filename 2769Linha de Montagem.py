import sys
while True:
    try:
        
        n = input()
        tempo = 0
        linha1 = False
        e1, e2 = map(int, input().split())
        
        tempo += min(e1, e2)
        
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
                    
        trocaA_B = list(map(int, input().split()))
        trocaB_A = list(map(int, input().split()))

        x1, x2 = map(int, input().split())
        if(e1 == e2):
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
        
        print(tempo)

    except EOFError:
        break