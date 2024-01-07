"""Sequencia de numero como entrada e retorne o fatorial desses numeros."""

incremento = 1
numero = 1

def fatorial(numero):
        
        decremento = numero
        if numero == 0:
            print(1)
        else:
            while decremento != 1 and numero != -1:
                decremento -= 1
                numero = numero * decremento
            return numero

while incremento <= 100 and numero != -1:
    numero = int(input("Digite números para fatorial: "))
    
    print(fatorial(numero))
    
    incremento += 1

