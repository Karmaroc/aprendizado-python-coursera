def n_primos(n):
    
    lista = []
    primos = []
    compostos = []

    for primo in range(2, n + 1):
        lista.append(primo)

    for i in lista:
        if (i % 2 == 0 and i != 2) or (i % 3 == 0 and i != 3) or (i % 5 == 0 and i != 5) or (i % 7 == 0 and i != 7) or (i % 11 == 0 and i != 11):
            compostos.append(i)       
        else:
            primos.append(i)

    return len(primos)

print(n_primos(2))
