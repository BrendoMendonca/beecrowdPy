from math import sqrt#importação da função sqrt
while(True):#estrutura de repetição para recebimento dos testes
    try:
        #recebimendo dos valores
        x_fid, y_fid, x_invasor, y_invasor, velocidade, raio_ult, raio_corvos = map(int, input().split())

        #calculo da distancia euclidiana
        distancia1 = sqrt((pow((x_invasor - x_fid), 2.0)) + (pow((y_invasor - y_fid), 2.0))) + (velocidade * 1.5)
        distancia2 = raio_ult + raio_corvos
        #verifica se a distancia do ataque chega até o invasor e exibe o resultado
        if(distancia2 >= distancia1):
            print('Y')
        else:
            print('N')
    except EOFError:
        break