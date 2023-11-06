alcool = gas = diesel = 0
while(True):
    tipo = int(input())
    if(tipo == 1):
        alcool += 1
    elif(tipo == 2):
        gas += 1
    elif(tipo == 3):
        diesel += 1
    elif(tipo == 4):
        break

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gas}")
print(f"Diesel: {diesel}")