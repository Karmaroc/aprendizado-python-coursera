largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

i = 1
a = ""

for x in range(0, altura):
    while i <= (largura):
        a += "#"
        i += 1    
    print(a)