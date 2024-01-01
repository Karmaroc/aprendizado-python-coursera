""" Dizemos que um número inteiro positivo é triangular se ele é o produto de três numeros inteiros consecutivos.
Por exemplo, 120 é triangular. Dado um número inteiro positivo n, verificar se n é triangular. """

import math

numero = int(input("Digite um número: "))

coeficiente_a = 1
coeficiente_b = 1
coeficiente_c = -(2 * numero)

bhaskara_delta = ((coeficiente_b) ** 2) - (4 * (coeficiente_a) * (coeficiente_c))

# print(bhaskara_delta)

if bhaskara_delta < 0:
    print("Sem raiz.")

elif bhaskara_delta == 0:
    raiz_quadrada = math.sqrt(bhaskara_delta)
    bhaskara_raiz1 = -(coeficiente_b) + raiz_quadrada / 2 * coeficiente_a
        
else:
    if bhaskara_delta > 0:
        raiz_quadrada = math.sqrt(bhaskara_delta)
        bhaskara_raiz1 = (-(coeficiente_b) + raiz_quadrada) / (2 * coeficiente_a) 
        bhaskara_raiz2 = (-(coeficiente_b) - raiz_quadrada) / (2 * coeficiente_a)

x1 = bhaskara_raiz1
x2 = bhaskara_raiz2

if x1.is_integer() or x2.is_integer():
    print("Triangular.")
else: 
    print("Não é Triangular.")            



