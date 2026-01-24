import re
cpf = input()
partes = re.split(r'[.-]', cpf)#separa a string quando houver ocorrência de "." e "-" do CPF
print(partes[0])
print(partes[1])
print(partes[2])
print(partes[3])