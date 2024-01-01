"""Desafio: Dado um número com vários dígitos, dizer se tem 2 dígitos adjacentes iguais ou não."""

numero = int(input("Digite um número inteiro: "))

inteiro = numero
anterior = numero % 10
resposta = False

while inteiro != 0:
    resto = inteiro % 100
    resto2 = resto // 10
    inteiro = inteiro // 10

    if resto2 == anterior:
        resposta = True
    else:
        anterior = resto2 
              

if resposta:
    print("sim")
else:
    print("não")        


    















# n_salvo = n = int(input("Digite um numero: "))

# anterior = n % 10
# n = n // 10;
# adj_iguais = False;
# pos = 0

# while n > 0 and not adj_iguais:
#     atual = n % 10
#     if atual == anterior:
#         adj_iguais = True
#     else:
#         pos += 1
#     anterior = atual
#     n = n // 10

# if adj_iguais:
#     print(n_salvo, "tem dois digitos", atual, "adjacentes")
# else:
#     print(n_salvo, "nao tem digitos iguais adjacentes")

