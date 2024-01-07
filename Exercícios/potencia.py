"""Dados números inteiros n e k, com k >= 0, calcular n elevado a k. 
Por exemplo, dados os números 3 e 4 o seu programa deve escrever o número 81"""

n = int(input("Digite um número n: "))
k = int(input("Digite um número k: "))

contador = 1
potencia = n

while contador <= k:
    contador += 1
    
    potencia = potencia ** k
    print(potencia)
    break

if k == 0:
    print(1)

