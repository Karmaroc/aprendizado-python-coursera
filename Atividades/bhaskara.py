import math 

a = int(input("Digite o coeficiente angular(a): "))
b = int(input("Digite o coeficiente linear(b): "))
c = int(input("Digite o coeficiente (c): "))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("esta equação não possui raízes reais")

elif delta == 0:
    raiz_quadrada = math.sqrt(delta)
    x1 = (-(b) + raiz_quadrada) / (2 * a)
    
    print(f"a raiz desta equação é {x1}")
    
else:
    if delta > 0:
        raiz_quadrada = math.sqrt(delta)
        x1 = (-(b) + raiz_quadrada) / (2 * a)
        x2 = (-(b) - raiz_quadrada) / (2 * a)
        
        if x1 < x2:
            print(f'as raízes da equação são {x1} e {x2}') 
        else:
            if x2 < x1:
                print(f'as raízes da equação são {x2} e {x1}')