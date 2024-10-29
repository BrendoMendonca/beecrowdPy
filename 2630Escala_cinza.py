t = int(input())
for i in range(t):
    
    escolha = input()
    rgb = list(map(int, input().split()))
    r, g, b = rgb   
    
    print(f"Caso #{i+1}:", end=" ")
    if escolha == 'eye':
        p = 0.30*r + 0.59*g + 0.11*b
        print(f"{int(p)}")
    elif escolha == 'mean':
        p = (r+g+b)/3
        print(f"{int(p)}")
    elif escolha == 'min':
        print(min(rgb))
    elif escolha == 'max':
        print(max(rgb))