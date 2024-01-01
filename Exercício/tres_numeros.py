"""Escreva um programa que leia três números inteiros e os imprima em ordem crescente."""

contador = 1

ordem1 = []
ordem2 = []
ordem3 = []

while contador < 4:

    
    numero = int(input("Digite 3 números para ordenar: "))
    
    if ordem1 == []: 
        ordem1.append(numero)
        ordem1 = int(ordem1[0])
        # print(ordem1)
    elif ordem2 == []:
        ordem2.append(numero)
        ordem2 = int(ordem2[0])
        # print(ordem1, ordem2)
    else:
        if ordem3 == []:
            ordem3.append(numero)
            ordem3 = int(ordem3[0])
            # print(ordem1, ordem2, ordem3)
    
    
    contador += 1
    
    
if ordem1 < ordem2 < ordem3:
    print(f'{ordem1}, {ordem2}, {ordem3}')
elif ordem1 < ordem3 < ordem2:
    print(f'{ordem1}, {ordem3}, {ordem2}')
elif ordem2 < ordem1 < ordem3:
    print(f'{ordem2}, {ordem1}, {ordem3}')
elif ordem2 < ordem3 < ordem1:
    print(f'{ordem2}, {ordem3}, {ordem1}')
elif ordem3 < ordem1 < ordem2:
    print(f'{ordem3}, {ordem1}, {ordem2}')
else:
    if ordem3 < ordem2 < ordem1:
       print(f'{ordem3}, {ordem2}, {ordem1}')
            
    