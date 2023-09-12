renda = float(input())

if(renda <= 2000):
    print("Isento")
else:
    if(renda > 2000 and renda <= 3000):
        imposto = (renda - 2000.0)*0.08
    elif(renda > 3000 and renda <= 4500 ): #se osalário estiver entre 3000.01 e 4500.00, calcula o imposto sobre a parte que excede 2000.00 e sobre a parte que excede 3000.00
        imposto = (renda - 3000.0)*0.18 + (1000*0.08)
    elif(renda > 4500): #se o salário for maior que 4500.00, calcula o imposto sobre a parte que excede 2000.00, 3000.00 e 4500.00
        imposto = (renda - 4500)*0.28 + (1500*0.18) + (1000*0.08)

    print(f"R$ {imposto:.2f}")