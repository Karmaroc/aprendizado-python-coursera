import math 

x = int(input("Digite um valor no eixo x1: "))
y = int(input("Digite um valor no eixo y1: "))

x2 = int(input("Digite um valor no eixo x2: "))
y2 = int(input("Digite um valor no eixo y2: "))

valores_x = x - x2
valores_y = y - y2

distancia_pontos = math.sqrt(((valores_x) ** 2 ) + ((valores_y) ** 2))

# print(distancia_pontos)

if distancia_pontos >= 10:
    print("longe")
else:
    if distancia_pontos < 10:
        print("perto")