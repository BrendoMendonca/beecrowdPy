qnt_jipe = 0
qnt_turista = 0
while True:
    jipe = input().split()
    caminho = jipe[0]
    if caminho == 'ABEND':
        break
    
    passageiros = int(jipe[1])
    
    if(caminho == 'SALIDA'):
        qnt_jipe += 1
        qnt_turista += passageiros
    elif(caminho == 'VUELTA'):
        qnt_jipe -= 1
        qnt_turista -= passageiros
    
print(qnt_turista)
print(qnt_jipe)