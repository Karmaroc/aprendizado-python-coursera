"""Dados dois inteiros positivos calcular o máximo divisor comum entre eles usando o algoritmo de Euclides."""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

resto = 1

while resto > 0:
    if n1 < n2:
        x = n1
        n1 = n2
    else:
        if n1 > n2:
            x = n2
        
    resto = n1 % x
    
    if resto == 0:
        break
    
    n2 = n2 % resto #12
    
    if n2 == 0 or n2 == 1:
        break
            
if n2 == 0:
    print("valor", resto)
else:
    if n2 == 1:
        print(n2)
    else:
        if resto == 0:
            print(n2)
    