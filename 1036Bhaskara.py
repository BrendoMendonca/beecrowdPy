valores = input()
a, b, c = map(float, valores.split())

delta = (float) (b**2) - (4*a*c)
x1 = (float)(-b + delta)/(2*a)
x2 = (-b - delta)/(2*a)

if(a == 0) or (delta < 0):
    print("Impossivel calcular")
else:
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")