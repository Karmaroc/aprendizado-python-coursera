def fatorial(n):
    contador = n 
    
    if n == 0:
        return 1
    else:
        while contador != 1:
            contador -= 1
            n = n * contador
    return n    
    

def combinacao(m, n):
    comb = fatorial(m) / (fatorial(m - n) * fatorial(n))
    return comb

print(combinacao(20, 2))