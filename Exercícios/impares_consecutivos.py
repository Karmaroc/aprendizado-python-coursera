"""
Ímpares consecutivos cuja soma é igual a n**3
"""
m = int(input("Digite um número: "))

formula = m ** 3

lista = []

for numero in range(1, formula):
    if numero % 2 != 0:
        lista.append(numero)

soma = 0
qtd = []

disposto = ""

for valor in lista:
    qtd.append(valor)
        
    if len(qtd) == m:
        for i in qtd:
            soma += i
        
        somas = soma
        
        if somas == formula:
            for a in qtd:
                a = str(a)
                disposto += a + " + "
                str_disposta = disposto[0:len(disposto) - 2]
            print(f"{m}**3 = {str_disposta}")
        
        if somas != formula:
            soma = 0
            qtd.pop(0)
        
        
            

            
        
            
                
             
            
        
        
        
        
                    
            
        
         
    




