n = int(input("Digite um número para decompor: "))

def fatores(n):
    
    lista = []
    
    for i in range(2, n + 1):
        while n % i == 0 and n != 1:
            n = n // i
            lista.append(i)
    return lista

def quantidade_fatores(n):
    dic_valor = {}
    lista = fatores(n)
    
    for valor in lista:
        
        if valor not in dic_valor.keys():
            dic_valor[valor] = 1
        else:
            dic_valor[valor] += 1
            
    return dic_valor

x = quantidade_fatores(n)

for chave, valor in x.items():
    print(f'fator {chave} multiplicidade {valor}')


    
    