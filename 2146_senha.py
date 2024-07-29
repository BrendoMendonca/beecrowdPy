while(True):#estrutra de repetição para recebiemnto dos casos
    try:
        n = int(input())#entrada do número
        print(n-1)#exibição da senha
    except EOFError:
        break