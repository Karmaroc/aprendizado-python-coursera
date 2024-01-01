"""Escreva um programa que leia três números naturais e
verifica se eles formam os lados de um triângulo retângulo."""

a = int(input("Lado A: "))
b = int(input("Lado B: "))
c = int(input("Lado C: "))

if (a ** 2) == (b ** 2) + (c ** 2):
    print("Triângulo Retângulo")
    
elif (b ** 2) == (a ** 2) + (c ** 2):
        print("Não é Triângulo Retângulo")
else:
    if (c ** 2) == (b ** 2) + (a ** 2):
        print("Triângulo Retângulo")
    else:
        print("Não é Triângulo Retângulo")
        