def verificar_experimentos():
    n = int(input())  #número de casos de teste

    for caso in range(n):
        t = int(input())  #número de compostos perigosos
        compostos_perigosos = [input().strip() for _ in range(t)]

        u = int(input())  #número de experimentos
        experimentos = [input().strip() for _ in range(u)]

        for experimento in experimentos:
            abortar = False
            for perigoso in compostos_perigosos:
                pos = experimento.find(perigoso)
                while pos != -1:
                    fim = pos + len(perigoso)
                    #se o composto perigoso for encontrado e for o fim da string ou for separado de outros compostos
                    if fim == len(experimento):
                        abortar = True
                        break
                    else:
                        #verifica se o resto da string forma outro composto perigoso
                        for outro_perigoso in compostos_perigosos:
                            if experimento[fim:].startswith(outro_perigoso):
                                abortar = True
                                break
                        if abortar:
                            break
                    #procura outra ocorrência do mesmo perigoso
                    pos = experimento.find(perigoso, pos + 1)
                if abortar:
                    break
            print("Abortar" if abortar else "Prossiga")
        
        if caso != n - 1:
            print()

verificar_experimentos()