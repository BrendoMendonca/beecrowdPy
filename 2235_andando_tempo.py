a, b, c = map(int, input().split())#recebimento dos créditos de viagem

#verifica se possui créditos com valores iguais, pois assim é possível fazer duas viagens
if(a == b or b == c or c == a):
    print("S")
#verifica se a soma de dois créditos resulta no terceiro valor e assim sendo permitido fazer 3 viagens
elif((a + b == c) or (b + c == a) or (c + a == b)):
    print("S")
else:
    print("N")