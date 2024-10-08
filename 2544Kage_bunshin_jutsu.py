from math import log
while True:
    try:
        n = int(input())
        resultado = log(n, 2)
        print(f"{resultado:.0f}")
    except EOFError:
        break