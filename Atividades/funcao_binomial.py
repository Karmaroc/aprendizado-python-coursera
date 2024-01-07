def fatorial(numero):
    
    contador = int(numero)
    fatorial = int(numero)

    if numero == 0:
        return 1
    else:
        while contador != 1:   
            contador = contador - 1
            fatorial = fatorial * contador 
            
        return fatorial

def binomial(n, k):
    if k == 0:
        return 1
    else:
        if k == 1:
            return n
        else:
            coeficiente = fatorial(n) // (fatorial(k) * fatorial(n - k))
            return coeficiente
        
# print(binomial(5, 3))
# print(binomial(10, 1))
# print(binomial(6, 2))
# print(binomial(5, 0))



