# Leitura do valor de ponto flutuante com duas casas decimais
valor_float = float(input())

# Convertendo o valor para centavos (inteiro)
valor_centavos = int(valor_float * 100)

# Lista das notas e moedas disponíveis em centavos
notas_centavos = [10000, 5000, 2000, 1000, 500, 200]
moedas_centavos = [100, 50, 25, 10, 5, 1]

# Dicionários para armazenar a quantidade de cada nota e moeda necessária
quant_notas = {}
quant_moedas = {}

# Cálculo da quantidade de cada nota
for nota in notas_centavos:
    quantidade = valor_centavos // nota
    valor_centavos %= nota
    quant_notas[nota] = quantidade

# Cálculo da quantidade de cada moeda
for moeda in moedas_centavos:
    quantidade = valor_centavos // moeda
    valor_centavos %= moeda
    quant_moedas[moeda] = quantidade

# Impressão da quantidade mínima de notas e moedas necessárias
print("NOTAS:")
for nota, quantidade in quant_notas.items():
    print(f"{quantidade} nota(s) de R$ {nota / 100:.2f}")

print("MOEDAS:")
for moeda, quantidade in quant_moedas.items():
    print(f"{quantidade} moeda(s) de R$ {moeda / 100:.2f}")