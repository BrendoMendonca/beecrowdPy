import sys #uso de método da biblioteca sys para acelerar o processamento de entrada e saída

#recebimento da entrada da primeira linha de dados usando o método sys.stdin.readline para tornar o código mais rápido
input = sys.stdin.readline 

def solve():
    while True:
        linha = input()
        if not linha:
            break
        
        try:
            x, y, m = [int(i) for i in linha.split()]#recebimento das medidas do cliente
            
            resultados = [] #lista para armazenar a aceitação do tamanho das placas
            for _ in range(m):
            
                xi, yi = [int(i) for i in input().split()]#recebimento das medidas do cliente
                
                if (xi <= x and yi <= y) or (xi <= y and yi <= x):
                    resultados.append("Sim")
                else:
                    resultados.append("Nao")

            sys.stdout.write("\n".join(resultados) + "\n")
            
        except (ValueError, EOFError):
            break

if __name__ == "__main__":
    solve()