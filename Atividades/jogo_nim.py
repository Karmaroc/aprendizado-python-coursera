def computador_escolhe_jogada(n, m):# m = numero maximo de peça retiradas e n = numero de peças dispostas 
    computador = 1
    
    while computador != m:
        if (n - computador) % (m + 1) == 0:
            return computador
        else:
            computador += 1
            
    return computador

def usuario_escolhe_jogada(n, m):
    validador = False
    
    while not validador:
        print("")
        jogada = int(input("Qual a sua jogada: "))
        if jogada > m or jogada < 1:
            print("")
            print("Oops! Tente de novo!")
        else:
            validador = True
            
    return jogada
             
        
def partida():
    
    n = int(input("Digite a quantidade de peças dispostas: "))
    m = int(input("Digite o limite máximo de retirada: "))
    
    validador = False
    
    if n % (m + 1) == 0:
        print("")
        print("Você começa!")
    else:
        print("")
        print("Computador começa!")
        validador = True
        
    while n > 0:

        if validador:
            computador_tira = computador_escolhe_jogada(n, m)
            n = n - computador_tira
            if computador_tira >= 1:
                print("")
                print(f"O computador tirou {computador_tira} peça(s).")
            
            validador = False
            
        else:
            usuario_tira = usuario_escolhe_jogada(n, m)
            n = n - usuario_tira
            if usuario_tira >= 1:
                print("")
                print(f"Você tirou {usuario_tira} peça(s).")
            
            validador = True
            
        if n != 0:
            print(f"Agora resta(m) {n} no tabuleiro.")
            
    if n == 0:
        print("")
        x = "O computador ganhou!"
        print(x)
          

def campeonato():
    quantidade = 1
    while quantidade <= 3:
        
        print("")
        print("/// RODADA", quantidade, "///")
        print("")
        partida()

        quantidade += 1 
        
    print(f"Placar: Você 0 X {quantidade - 1} Computador")
    

print("")
print("Bem-vindo: Que os jogos comecem! Escolha: ", end="\n\n")    
print("Digite [1] para jogar isolado.")
print("Digite [2] para jogar um campeonato.", end="\n\n")    

numero = int(input("Escolha 1 ou 2: "))

if numero == 1:
    print("")
    print("Você escolheu jogar isolado!", end="\n\n")
    partida()
else:
    if numero == 2:
        print("")
        print("Você escolheu jogar um campeonato!")
        campeonato()