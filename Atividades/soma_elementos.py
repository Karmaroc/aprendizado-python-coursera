def soma_elementos(lista):
    soma = 0
    
    for numero in lista:
        soma = soma + numero
    
    return soma    

print(soma_elementos([10, 20, 50, 50, 100, 70, 15]))