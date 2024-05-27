def int_to_roman(num):
    #mapeamento dos valores arábicos para os respectivos símbolos romanos
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    rom = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_num = ''
    i = 0
    while num > 0:#o num é decrementado até que seja zero
        for _ in range(num // val[i]):#laço de repetição para adicionar os símbolos romanos correspondetes
            roman_num += rom[i]
            num -= val[i]
        i += 1
    return roman_num

#Leitura do número de entrada
N = int(input())

  #impressão do resultado
print(int_to_roman(N))