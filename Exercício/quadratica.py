import math 

a = int(input("Digite o coeficiente angular(a): "))
b = int(input("Digite o coeficiente linear(b): "))
c = int(input("Digite o coeficiente (c): "))

delta = (b ** 2) - (4 * a * c)

print("=============================")
print(f"{a}x^2 + {b}x + {c} = 0")
print(f"Delta: {delta}")
print("=============================")

if delta < 0:
    print("Não tem raízes reais.")

elif delta == 0:
    raiz_quadrada = math.sqrt(delta)
    x1 = (-(b) + raiz_quadrada) / (2 * a)

    print(f'Tem apenas uma raíz real: {x1:.2f}')
else:
    if delta > 0:
        raiz_quadrada = math.sqrt(delta)
        x1 = (-(b) + raiz_quadrada) / (2 * a)
        x2 = (-(b) - raiz_quadrada) / (2 * a)
        
        print(f'Tem duas raízes reais: {x1:.2f} e {x2:.2f}')        
