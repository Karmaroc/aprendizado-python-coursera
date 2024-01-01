def primeiro_trio(hipo):
    # m e n ímpares
    m = 3
    n = 1 
    e = 1 / 2
    c = 0
    validador = True
    lista = []
    
    while c < hipo and validador:
       
        if m % 2 != 0 and n % 2 != 0: 
            a = 2 * e * m * n
            b = e * (m ** 2 - n ** 2)
            c = e * (m ** 2 + n ** 2)
            a;
            b;
            
            c = int(c)
                
            lista.append(c)
            
            if c > hipo:
                lista.pop()
        m += 1
        n += 1
                        
    return lista

def segundo_trio(hipo):
    m = 3
    n = 1
    k = 2
    validador = True
    e = 1 / 2
    c = 0
    lista2 = []
    
    while c < hipo and validador:
        a = 2 * e * m * n
        b = e * (m ** 2 - n ** 2)
        c = e * (m ** 2 + n ** 2)
        a;
        b;
        c = c * k
        c = int(c)
        
        lista2.append(c)
        
        if c > hipo:
            lista2.pop()
      
        k += 1
    
    return lista2 

def terceiro_trio(hipo):
    c = 0
    validador = True
    lista3 = []
    e = 1 / 2
    m = 5
    n = 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    
    while c < hipo and validador:
        
        if m % 2 != 0 and n % 2 != 0:
            a = 2 * e * m * n
            b = e * (m ** 2 - n ** 2)
            c = e * (m ** 2 + n ** 2)
            a;
            b;
            c = int(c)
        
            lista3.append(c)  
            
            if c > hipo:
                lista3.pop()      
    
        m += 1
        n += 1
    
    return lista3

def quarto_trio(hipo):
    c = 0
    validador = True
    lista4 = []
    e = 1 / 2
    m = 5
    n = 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    k = 2
    while c < hipo and validador:
        a = 2 * e * m * n
        b = e * (m ** 2 - n ** 2)
        c = e * (m ** 2 + n ** 2)
        a;
        b;
        c = int(c) * k
        
        lista4.append(c)  
            
        if c > hipo:
            lista4.pop()      
    
        k += 1
    
    return lista4

def é_hipotenusa(hipotenusa):
    
    x1 = primeiro_trio(hipotenusa)
    x2 = segundo_trio(hipotenusa)
    x3 = terceiro_trio(hipotenusa)
    x4 = quarto_trio(hipotenusa)
    
    resultado = x1 + x2 + x3 + x4
    
    resultado = [i for i in resultado if i != []]
    
    resultado_novo = list(set(resultado))
    
    resultado_novo.sort()
    
    return resultado_novo

def soma_hipotenusas(numero):
    
    soma = 0
    
    for valor in é_hipotenusa(numero):
        
        soma += valor
    
    return soma

print(soma_hipotenusas(100))

    
  

 