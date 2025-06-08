import re

# 4.51, 0.693, 0.55, 70.82, 1.82, 38.5

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    print("")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))
    print("")
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
        print("")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def total_palavras(texto):

    resultado = len(texto.split())
    return resultado

def lista_palavras(texto):
    resultado = texto.split(" ")
    return resultado

def tam_med_pal(texto):
    soma = 0
    total_pal = 0

    for sentencas in separa_sentencas(texto):
        for frase in separa_frases(sentencas):
            for palavra in separa_palavras(frase):
                total_pal += 1
                comp = len(palavra) 
                soma += comp

    return soma / total_pal

def type_token(texto):
    novo_texto = re.sub(r'[^\w\s]', '', texto)
    lista = lista_palavras(novo_texto)
    return n_palavras_diferentes(lista) / total_palavras(novo_texto)

def hapax(texto):
    novo_texto = re.sub(r'[^\w\s]', '', texto)
    apenas_uma = lista_palavras(novo_texto)
    return n_palavras_unicas(apenas_uma) / total_palavras(novo_texto)

def tamanho_sentenca(texto):
    soma = 0
    for sentenca in separa_sentencas(texto):
        comp = len(sentenca)
        soma += comp

    div_sentenca = len(separa_sentencas(texto))
    
    return soma / div_sentenca

def complex_media(texto):
    lista_de_sent = separa_sentencas(texto)
    
    lista = []
    nova_soma = 0

    for sentenca in lista_de_sent:
        nova_soma += 1
        frases = separa_frases(sentenca)
        lista.append(frases)

    soma = 0

    for sublista in lista:
        for frase in sublista:
            soma += 1

    return soma / nova_soma

def tamanho_medio_frase(texto):
    lista_de_sent = separa_sentencas(texto)

    lista = []

    for sentenca in lista_de_sent:
        frases = separa_frases(sentenca)
        lista.append(frases)

    soma2 = 0
    soma = 0

    for sublista in lista:
        for frase in sublista:
            soma2 += 1
            comp = len(frase)
            soma += comp

    return soma / soma2

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    
    soma_a = 0

    for a in as_a:
        soma_a += a

    as_a = soma_a
    
    soma_b = 0

    for b in as_b:
        soma_b += b

    as_b = soma_b

    grau_ass = abs(as_a - as_b) / 6

    return grau_ass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    return [tam_med_pal(texto), type_token(texto), hapax(texto), tamanho_sentenca(texto), complex_media(texto), tamanho_medio_frase(texto)]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    graus = []
    lista_ass = []
    for texto in textos:
        assinatura = calcula_assinatura(texto)
        lista_ass.append(assinatura)
        grau = compara_assinatura(ass_cp, assinatura)
        graus.append(grau)

    menor_grau = min(graus)

    for assin in lista_ass:
        if compara_assinatura(ass_cp, assin) == menor_grau:
            assin;

    numero_txt = graus.index(menor_grau) + 1

    return f"A assinatura de texto é: {assin}.\n" f"O grau de similaridade é: {menor_grau}.\n" f"O texto {numero_txt} está com o maior caso de COH-PIAH."
    
ass_cp = le_assinatura()
textos = le_textos()

print(avalia_textos(textos, ass_cp))