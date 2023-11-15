s = 1
num = 3
den = 2

while(True):
    s += num/den
    if(num == 39):
        break
    num += 2
    den *= 2

print(f"{s:.2f}")