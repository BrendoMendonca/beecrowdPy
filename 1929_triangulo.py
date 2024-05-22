def forma_triangulo(a, b, c):#função que verifica se as medidas formam um triângulo de acordo com as condições de formação dos triângulos
    return(a + b > c) and (a + c > b) and (b + c > a)

def verifica(a, b, c, d):#função que verifica a formação dos triangulos de acordo com o resultado da função anterior
    if(forma_triangulo(a, b, c)):
        return 'S'
    if forma_triangulo(a, b, d):
        return 'S'
    if forma_triangulo(a, c, d):
        return 'S'
    if forma_triangulo(b, c, d):
        return 'S'
    return 'N'

valores = input().split()#recebimento dos valores
a, b, c, d = map(int, valores)

print(verifica(a, b, c, d))#imprime o resultado