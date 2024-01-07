n = int(input("Limite máximo de números Primos: "))

def ehPrimo(n):
    for i in range(2, n):
        if i != 1 and i != n and n % i == 0:
            return False
                                            
    return True

print(ehPrimo(n))

lista_de_primos = []

for primo in range(2, n + 1):
    if ehPrimo(primo):
        lista_de_primos.append(primo)

print(lista_de_primos)
