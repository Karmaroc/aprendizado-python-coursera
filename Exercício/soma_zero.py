""" Dada uma sequência de números inteiros diferentes de zero, terminada por um zero, calcular a sua soma. Por exemplo, para a sequência:
"""

numero = input("Digite um número: ")

inteiro = int(numero)
soma = 0
zero = False

while inteiro != 0:
    resto = inteiro % 10
    soma = soma + resto
    inteiro = inteiro // 10

contador = 0
num = []

while contador < len(numero):
    x = int(numero[contador])
    num.append(x)    
    if num[-1] == 0:
        zero = True
    contador += 1

if zero:
    print(soma)
else:    
    print("Não termina em zero.")
    
    
    
