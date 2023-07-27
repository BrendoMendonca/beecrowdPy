valores = input()
a, b, c = map(float, valores.split())

area_triang = (a*c)/2
area_cir = 3.14159 * c**2
area_trap = ((a + b)*c)/2
area_quad = b**2
area_ret = a * b

print(f"TRIANGULO: {area_triang:.3f}")
print(f"CIRCULO: {area_cir:.3f}")
print(f"TRAPEZIO: {area_trap:.3f}")
print(f"QUADRADO: {area_quad:.3f}")
print(f"RETANGULO: {area_ret:.3f}")