positivos = media = 0

for i in range (0, 6):

    num = float(input())
    if(num > 0):
        positivos +=1
        media += num

media =  media/positivos
print(f"{positivos} valores positivos")
print(f"{media:.1f}")