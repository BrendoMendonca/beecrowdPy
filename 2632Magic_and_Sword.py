def calcula_dano(T, caso_teste):
    #dicionário com as informações de dano e alcance por magia e nível
    poderes = {
        "fire": {"dano": 200, "raio": [20, 30, 50]},
        "water": {"dano": 300, "raio": [10, 25, 40]},
        "earth": {"dano": 400, "raio": [25, 55, 70]},
        "air": {"dano": 100, "raio": [18, 38, 60]},
    }

    resultados = []

    for i in range(T):
        #leitura dos dados do caso de teste
        w, h, x0, y0 = caso_teste[i]["retangulo"]
        magia, level, cx, cy = caso_teste[i]["magia"]
        level = int(level) - 1  # Ajustar o nível para índice (0, 1 ou 2)

        # Coordenadas do círculo e do retângulo
        raio = poderes[magia]["raio"][level]
        dano = poderes[magia]["dano"]

        # Verificar se há interseção entre o círculo e o retângulo
        x1, y1 = x0 + w, y0 + h

        #calcula a distância mínima entre o círculo e o retângulo
        distancia_x = max(x0, min(cx, x1))
        distancia_y = max(y0, min(cy, y1))
        distancia = (cx - distancia_x) ** 2 + (cy - distancia_y) ** 2

        if distancia <= raio ** 2:
            resultados.append(dano)
        else:
            resultados.append(0)

    return resultados

#entrada de dados
T = int(input())
caso_teste = []

for _ in range(T):
    #dimensões e coordenadas do retângulo
    retangulo = tuple(map(int, input().split()))
    #informações sobre a magia
    magia_data = input().split()
    magia = magia_data[0]
    level = magia_data[1]
    cx, cy = map(int, magia_data[2:])
    caso_teste.append({"retangulo": retangulo, "magia": (magia, level, cx, cy)})

#impressão dos resultados
resultados = calcula_dano(T, caso_teste)
for result in resultados:
    print(result)
