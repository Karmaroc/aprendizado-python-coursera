validador = True

while validador:
    ano = input("Digite um ano qualquer ou 'sair': ")
    
    if ano == "sair":
        validador = False 
        break 
    
    excecao = (int(ano) % 100 == 0) and (int(ano) % 400 == 0) 
    
    if int(ano) % 4 == 0 and excecao:
        print("Esse ano é Bissexto:", True)
    elif True:
        if int(ano) % 4 == 0 and int(ano) % 100 != 0: # A excecao calcula anos terminados em 00. 
            print("Esse ano é Bissexto:", True)       # Anos que não são multiplos de 100 e ainda são multiplos de 4 retornnam True. Ex. 2016 ou
        else:
            print("Esse ano não é Bissexto:", False)
    