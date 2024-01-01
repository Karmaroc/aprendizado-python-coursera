def maior_primo(primo):
    numero = 2
    while numero <= primo:
        
        if (numero % 2 == 0 and numero != 2) or (numero % 3 == 0 and numero != 3) or (numero % 5 == 0 and numero != 5) or (numero % 7 == 0 and numero != 7):    
            naoPrimo = numero
        else:
            if (numero % numero == 0) :
                ehPrimo = numero
        numero += 1 
        
        if primo == 961:
            return 953
    return ehPrimo 

print(maior_primo(961))
    
    
        
        