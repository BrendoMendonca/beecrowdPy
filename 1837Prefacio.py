a, b = map(int, input().split())

#calculo do quociente e do resto
q = a // b
r = a % b

#garante que o resto e o quociente estão no intervalo especificado
if r < 0:
    r += abs(b)
    if b < 0:
        q += 1

print(f"{q} {r}")