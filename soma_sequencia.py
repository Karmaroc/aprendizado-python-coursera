n = int(input("Digite um número para a sequência: "))

contador = 1
lista = []

while contador <= n:
    numeros = int(input("Digite um novo número: "))
    lista.append(numeros)
    contador += 1

# lista = [5, -2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1]

soma = 0 
i = 0
nova = []
nova_completo = []

while i < len(lista):
    lista2 = lista[i:]
    soma = sum(lista2)
    
    nova.append(soma)
    nova_completo.append(lista2)
    i += 1

a = len(lista) - 1
nova1 = []
nova1_completo = []

while a > 0:
    lista3 = lista[:a]
    soma1 = sum(lista3)
    
    nova1.append(soma1)
    nova1_completo.append(lista3)
    
    a = a - 1 

n = 0
z = 1
nova2 = []
nova2_completo = []

while len(lista) - n > 0 and z < len(lista):
    y = len(lista) - n
    
    lista4 = lista[z:y]
    soma2 = sum(lista4)        
    nova2.append(soma2)
    nova2_completo.append(lista4)
    
    n += 1
    z += 1

nova3 = []
p = 0
b = 1
nova3_completo = []

while len(lista) - b > 0 and p < len(lista):
    c = len(lista) - b
    
    lista5 = lista[p:c]
    soma3 = sum(lista5)        
    
    nova3.append(soma3)
    nova3_completo.append(lista5)
    
    b += 1
    p += 1

nova4 = []
v = 1
m = 1
nova4_completo = []

while len(lista) - m > 0 and v < len(lista):
    r = len(lista) - m 
    
    lista6 = lista[v:r]
    soma4 = sum(lista6)
    
    nova4.append(soma4)
    nova4_completo.append(lista6)
    v += 1
    m += 1

max_number = nova + nova1 + nova2 + nova3 + nova4
max_lista = nova_completo + nova1_completo + nova2_completo + nova3_completo + nova4_completo

resultado = max(max_number)

for indice in max_lista:
    if max(max_number) == sum(indice):
        lista_numero = max_lista.index(indice)

texto = ""

for elemento in max_lista[lista_numero]:
    elemento = str(elemento)
    texto += elemento + " + "

x = texto.replace(" + -", " - ")
mensagem = x[:len(x) - 3]

print(lista)
print("")

print(f'{mensagem} = {resultado}')

        
        

            



