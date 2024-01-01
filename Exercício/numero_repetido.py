""" Dados um número inteiro n, n > 0, e um dígito d. 0 <= d <= 9, determinar quantas vezes d ocorre em n. """

validador = True

while validador:
    
    n = input("Digite um número inteiro: ")
    
    if n == "sair":
        break
    
    d = input("Digite um número inteiro de ocorrência: ")
    
    lista_numeros = list(n)
    num_encontrado = lista_numeros.count(d)

    print(f'O número {d} ocorreu {num_encontrado}x.')


