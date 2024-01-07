n = 1
lista = []

while n > 0:
    n = input("Digite um número: ")
    if n == 0:
        break
    
    n = int(n)
    lista.append(n)
lista.pop()
    
nova = []

for numero in lista:
    if (numero % 2 == 0 and numero != 2) or (numero % 3 == 0 and numero != 3) or (numero % 5 == 0 and numero != 5) or (numero % 7 == 0 and numero != 7) or (numero % 11 == 0 and numero != 11):
        print(numero, "Não é")
    else:
        if numero % numero == 0:
            print(numero, "É")
            nova.append(numero)        
        
print(len(nova), "elementos:", nova)