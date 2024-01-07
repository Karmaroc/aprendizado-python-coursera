import math 

def delta(a, b, c):
    
    delta = (b ** 2) - (4 * a * c)
    
    if delta < 0:
        return "sem raízes"

    raiz_quadrada = math.sqrt(delta)

    x1 = (-(b) + raiz_quadrada) / (2 * a)
    x2 = (-(b) - raiz_quadrada) / (2 * a)
        
    if delta == 0:
        return (f'A raíz é: {x1}')
    else:
        if delta > 0:
            if x1 < x2:
                return (f'As raízes é: {x1} e {x2}') 
            else:
                if x2 < x1:
                    return (f'As raízes é: {x2} e {x1}')   

print(delta(2, -7, 10))


