n = 1
lista = []

while n > 0 and n != "sair":
    n = input("Digite um número para MDC: ")
    if n == "sair":
        break
    
    n = int(n)
    lista.append(n)
    
def mdc(lista):
    num1 = lista[0]
    num = lista[1]
        
    resto = 1
        
    while resto > 0:
        resto = num1 % num
    
        if resto == 0: 
            break
    
        num = num % resto
    
        if resto > 0:
            num1 = resto
    
        if num == 0 or num == 1:
            break

    if num == 0:
        return resto
    else:
        if num == 1 or resto == 0: # Nesse caso, num valendo 1 é retornado pelos primos entre si.
            return num
        

def mdc_varios(lista):
    mdc_anterior = mdc(lista)
    indice = 1
    
    if len(lista) == 2:
        return mdc_anterior
    else:
        while indice < len(lista) - 1:
            indice += 1
            
            num1 = mdc_anterior 
            num = lista[indice]
            
            resto = 1
        
            while resto > 0:
                resto = num1 % num
    
                if resto == 0: 
                    break
    
                num = num % resto
    
                if resto > 0:
                    num1 = resto
    
                if num == 0 or num == 1:
                    break

            if num == 0:
                return resto
            else:
                if num == 1 or resto == 0: # Nesse caso, num valendo 1 é retornado pelos primos entre si.
                    return num 

         
print(mdc_varios(lista))