numero = int(input("Digite um número inteiro: "))

inteiro = numero
soma = 0

while inteiro != 0:
    resto = inteiro % 10
    soma = soma + resto
    inteiro = inteiro // 10
    
print(soma)