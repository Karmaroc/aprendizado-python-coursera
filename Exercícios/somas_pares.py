""" Dados um número inteiro n, n > 0, e uma sequência com n números inteiros, determinar a soma dos pares."""

numeros = input("Digite uma sequência de numeros inteiros: ")

lista = list(numeros)

pares = []

indice = 0

while indice < len(numeros):
    x = int(lista[indice])
    
    if x % 2 == 0 and x > 0:
        pares.append(x)

    indice += 1

# print(pares)

soma = sum(pares)
print("Soma dos pares:", soma)

    
    