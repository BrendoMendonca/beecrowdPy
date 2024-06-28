while True:#estrutura de repetição para realização dos casos
    try:
        
        vol = float(input())#recebimento do valor do volume
        diam = float(input())#recebimento do diâmetro
        
        raio = diam/2#calculo do raio do cilindro
        area = raio**2 * 3.14#calculo da área
        altura = vol/area#calculo da altura
        
        #exibição dos resultados
        print(f"ALTURA = {altura:.2f}")
        print(f"AREA = {area:.2f}")
        
    except EOFError:
        break