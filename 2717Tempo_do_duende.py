tempo_fim = int(input())
tempo1, tempo2 = map(int,input().split())

if(tempo_fim >= tempo1+tempo2):
    print("Farei hoje!")
else:
    print("Deixa para amanha!")