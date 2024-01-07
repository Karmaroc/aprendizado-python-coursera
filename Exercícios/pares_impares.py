"""Dados um número inteiro n, n > 0, e uma sequência com n números inteiros,
determinar quantos números da sequência são pares e quantos são ímpares."""

numeros = input("Digite uma sequência de números: ")

lista_numero = list(numeros)

indice = 0

pares = []
impares = []

while indice < len(lista_numero):
    x = int(lista_numero[indice])
    
    if x % 2 == 0 and x > 0:
        pares.append(x)
    else:
        if x > 0:
            impares.append(x)
    
    indice += 1

qtd_pares = len(pares)
qtd_impar = len(impares)

print("pares:", qtd_pares, "impares:", qtd_impar)
    

    
