media = quant = 0
while(True):
    idade = int(input())
    if(idade < 0):
        break
    media += idade
    quant += 1
media = media/quant
print(f"{media:.2f}")