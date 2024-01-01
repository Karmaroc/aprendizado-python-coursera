largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

i = 1

while i <= altura:        
    a = "#" * largura
    
    if i > 1 and i < altura:
        a = "#" + " " * (largura - 2) + "#"
    
    print(a)
    i += 1
    
    
    
        
        
    