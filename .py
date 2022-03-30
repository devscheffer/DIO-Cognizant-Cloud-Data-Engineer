#TODO: Complete os espaços em branco com uma solução possível para o problema.
for i in range(1):
    x, y = '56234523485723854755454545478690', '78690'
    teste = 0
    cont = 0
    if   len(x) < len(y)    :
        print("nao encaixa")

    else:
        for j in range(      len(y)):
            teste -= 1
            if x[teste] == y[teste]:
                cont += 1

        if  cont==len(y)      :
            print("encaixa")

        else:
            print("nao encaixa")
