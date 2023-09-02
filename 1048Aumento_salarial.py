sal = float(input())

if(sal <= 400):
    novo_sal = sal*1.15
    porcentagem = 15
elif(sal > 400 and sal <= 800):
    novo_sal = sal*1.12
    porcentagem = 12
elif(sal > 800 and sal <= 1200):
    novo_sal = sal*1.1
    porcentagem = 10
elif(sal > 1200 and sal <= 2000):
    novo_sal = sal*1.07
    porcentagem = 7
else:
    novo_sal = sal*1.04
    porcentagem = 4

ajuste = novo_sal - sal

print(f"Novo salario: {novo_sal:.2f}")
print(f"Reajuste ganho: {ajuste:.2f}")
print(f"Em percentual: {porcentagem} %")