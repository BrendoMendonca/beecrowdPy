n = int(input())#recebimento da quantidade de alunos
maior = 0#variável que representa a maior nota dos alunos
escolhido = 'Minimum note not reached'#inicialmente o escolhido não tem nota suficiente
for i in range(n):#estrutura de repetição para recebimento das matrículas e notas
    matricula, nota = map(float, input().split())#recebimento da matrícula e da nota em float
    if(nota > maior and nota >= 8):#verifica se a nota está de acordo com as condições
        maior = nota #a variável "maior" recebe a nota atual
        matricula = int(matricula) #transforma a matrícula em inteiro
        escolhido = str(matricula)#recebe o valor da matrícula do escolhido como str

print(escolhido)#exibe a matrícula do escolhido