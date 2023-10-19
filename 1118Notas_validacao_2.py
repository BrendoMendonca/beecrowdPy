while True: #laço de repetição que será executado até a solicitação de saída no fim    
    media = validas = 0 #a soma em cada repetição é zerada
    while True: #laço de repetição para capturar as notas dos alunos
        nota = float(input()) #recebimento das notas
        if(nota < 0 or nota > 10): #verifica se a nota é válida
            print("nota invalida")
        
        else: #incremento da média e da quanitdade de notas válidas
            media += nota
            validas += 1
        
        if(validas == 2): #verifica se atingiu a quantidade máxima de notas válidas
            break

    media /= 2 #cálculo da média
    print(f"media = {media:.2f}") #exibição da média

    print("novo calculo (1-sim 2-nao)")
    novo_cal = int(input())
    if(novo_cal == 2):
        break
    else:
        while(novo_cal != 1):
            print("novo calculo (1-sim 2-nao)")
            novo_cal = int(input())