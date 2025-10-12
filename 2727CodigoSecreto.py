import string

letras = string.ascii_lowercase #recebe as letras do alfabeto em minusculo
while True:
    try:
        def decodificador(pontos):#recebe a mensagem em forma de pontos
            grupos = pontos.split(' ')#separa os pontos por grupos
            #verifica a quantidade de grupos
            num_grupos = len(grupos)
            contador = len(grupos[0])
            #calculo para pegar a letra correspondente aos pontos do código
            indice_final = ((num_grupos - 1) * 3) + (contador - 1)
            return letras[indice_final]

        def main():
                
                n = int(input())#recebe a quantidade de letras que tem no código
                for _ in range(n):
                    codigo = input()#recebe o código
                    print(f"{decodificador(codigo)}")

        if __name__ == "__main__":
            main()
    except EOFError:
        break         