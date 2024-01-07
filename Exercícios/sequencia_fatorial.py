n = 1
lista = []

while n > 0 and n != "sair":
    n = input("Digite um número para Fatorial: ")
    if n == "sair":
        break
    
    n = int(n)
    
    contador = int(n)
    fatorial = int(n)

    if n == 0:
        print(1)
    else:
        while contador != 1:   
            contador = contador - 1
            fatorial = fatorial * contador
    
    print(fatorial)

