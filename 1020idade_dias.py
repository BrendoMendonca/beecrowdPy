idade = int(input())

anos = idade // 365
idade %= 365

meses = idade // 30
idade %= 30

dias = idade

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")