t = int(input())#recebimento da quantidade de casos teste
for i in range(t):#loop para recebimento e verificação dos valores
    sheldon, raj = map(str, input().split())#recebimento do personagem de cada um
    #verificação de cada caso
    if(sheldon == raj):
        print(f"Caso #{i+1}: De novo!")

    elif(sheldon == "tesoura"):
        if(raj == "papel" or raj == "lagarto"):
            print(f"Caso #{i+1}: Bazinga!")
        else:
            print(f"Caso #{i+1}: Raj trapaceou!")
    
    elif(sheldon == "papel"):
        if(raj == "pedra" or raj == "Spock"):
            print(f"Caso #{i+1}: Bazinga!")
        else:
            print(f"Caso #{i+1}: Raj trapaceou!")
    
    elif(sheldon == "pedra"):
        if(raj == "lagarto" or raj == "tesoura"):
            print(f"Caso #{i+1}: Bazinga!")
        else:
            print(f"Caso #{i+1}: Raj trapaceou!")
    
    elif(sheldon == "lagarto"):
        if(raj == "papel" or raj == "Spock"):
            print(f"Caso #{i+1}: Bazinga!")
        else:
            print(f"Caso #{i+1}: Raj trapaceou!")
    
    elif(sheldon == "Spock"):
        if(raj == "tesoura" or raj == "pedra"):
            print(f"Caso #{i+1}: Bazinga!")
        else:
            print(f"Caso #{i+1}: Raj trapaceou!")
