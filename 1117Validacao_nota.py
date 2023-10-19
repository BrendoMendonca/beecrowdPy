media = validas = 0
while True:
    nota = float(input())
    if(nota < 0 or nota > 10):
        print("nota invalida")
    
    else:
        media += nota
        validas += 1
    
    if(validas == 2):
        break
media /= 2
print(f"media = {media:.2f}")