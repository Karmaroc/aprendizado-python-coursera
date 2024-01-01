numero = int(input("Digite um número: "))
print("")

def fator_primo(n):
    primo = []
    
    for i in range(2, n + 1):
        while n % i == 0 and n != 1:
            n = n // i
            primo.append(i)
    return primo

def lista(x):
    incremento = 0
    lista_nova = []
    
    while incremento < len(fator_primo(x)):
        item = str(fator_primo(x)[incremento])
        lista_nova.append(item)
        incremento += 1
    return lista_nova

def exe(numero):
    texto = ""
    
    for fator in lista(numero):
        texto += " x " + fator

    x = texto[:0] + texto[:1] + texto[3:]
    
    return print(f"O decomposição de {numero} ={x}")

exe(numero)

    
    