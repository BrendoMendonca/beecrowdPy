n = int(input())#recebimento da quantidade de casos teste
for _ in range(n):
    num1, num2 = map(int, input().split())#recebimento dos números
    soma = num1 + num2
    #verifica o valor da soma dos números e exibe o resultado
    if soma == 0:
        print("PROXYCITY")
    elif soma == 1:
        print("P.Y.N.G.")
    elif soma == 2:
        print("DNSUEY!")
    elif soma == 3:
        print("SERVERS")
    elif soma == 4:
        print("HOST!")
    elif soma == 5:
        print("CRIPTONIZE")
    elif soma == 6:
        print("OFFLINE DAY")
    elif soma == 7:
        print("SALT")
    elif soma == 8:
        print("ANSWER!")
    elif soma == 9:
        print("RAR?")
    else:
        print("WIFI ANTENNAS")