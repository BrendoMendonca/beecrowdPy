for i in range(3):
    num = 0
    while(True):
        entrada = input()
        if(entrada[0] == '*'):
            num += 4
        if(entrada[2] == '*'):
            num += 1
        if(entrada == "caw caw"):
            print(num)
            break