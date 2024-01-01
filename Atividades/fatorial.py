n = int(input("Digite o valor de n: "))

contador = n
fatorial = n

if n == 0:
    print(1)
else:
    if n >= 1:
        while contador != 1:
            if n > 0:
                contador = contador - 1
                fatorial = fatorial * contador 
        
        print(fatorial) 
            
    
