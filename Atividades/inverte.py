n = 1
lista = []

while n != 0:
    n = int(input('Digite um número: '))
    lista.append(n)

lista.pop()

lista.reverse()

for num in lista:
    print(num)


