#Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
num = int(input())
hora = int(input())
valor = float(input())
salario = hora * valor

print(f"NUMBER = {num}")
print(f"SALARY = U$ {salario:.2f}")