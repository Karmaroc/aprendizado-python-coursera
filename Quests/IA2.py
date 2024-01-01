"""Dado um número inteiro de entrada n , crie um loop while que utiliza aritmética para armazenar a 
frequência de cada dígito presente em n em um dicionário Frequency_map.
O número de entrada n será fornecido como um tipo de dados numérico, não uma string. 
Para cada iteração do loop , você deve atualizar Frequency_map antes de reduzir n ."""

"""
digit = n mod 10

if digit is not in frequency_map keys

n = n // 10

else add 1 to the value of digit in frequency_map

while n is greater than 0

initialize an empty dictionary frequency_map

add digit to frequency_map with an initial value of 1

"""


n = int(input("Digite: "))

frequency_map = {}


while n > 0:
    
    digito = n % 10
    n = n // 10
    
    if digito not in frequency_map.keys():
        frequency_map[digito] = 1

    else:
        frequency_map[digito] += 1
    
print(frequency_map)
  


