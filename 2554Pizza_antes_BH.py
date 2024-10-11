while True:
    try:
        n_pessoas, n_datas = map(int, input().split())#recebimento da quantidade de pessoas
        data_encontro = "Pizza antes de FdI" #inicialmente a data do encontro não é estabelecida
        
        for _ in range(n_datas):
            resposta = input().split()#recebimento das datas e respostas das pessoas
            confirma = resposta.count("1")
            if confirma == n_pessoas and len(data_encontro) > 9: #verifica se todas as pessoas podem participar na data e se já possui uma data definida
                data_encontro = resposta[0]
        print(data_encontro)#exibe o resultado
                  
    except EOFError:
        break