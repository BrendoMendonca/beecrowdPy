texto = input()#recebimento do texto
if(len(texto) > 140):#verifica se o texto possui mais de 140 caracteres
    print("MUTE")
else:
    print("TWEET")