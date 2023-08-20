#entrada solicitada(2 inteiros)
valores = input()
#variáveis com o código e quantidade
cod, quant = map(int, valores.split())
#função para verificar qual o código informado e calcular o total do pedido
def verificacao(cod):
    match cod:
        case 1:
            total = 4.0*quant
        case 2:
            total = 4.5*quant
        case 3:
            total = 5.0*quant
        case 4:
            total = 2.0*quant
        case 5:
            total = 1.5*quant
    return print(f"Total: R$ {total:.2f}")
#chamanda da função
verificacao(cod)