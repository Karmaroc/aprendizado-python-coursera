""" Receba como entrada uma quantidade de segundos, converta em uma saída de: meses, semanas, dias, horas, minutos e segundos. """

condicao = True

while condicao:
    quantidade_segundos = int(input("Entre com um valor de segundos: "))

    if quantidade_segundos == "sair":
        condicao = False

    meses = quantidade_segundos // 2592000
    resto_meses_segundos = quantidade_segundos % 2592000
    semanas = resto_meses_segundos // 604800
    resto_semanas_segundos = resto_meses_segundos % 604800
    dias = resto_semanas_segundos // 86400
    resto_dias_segundos = resto_semanas_segundos % 86400
    horas = resto_dias_segundos // 3600
    resto_horas_segundos = resto_dias_segundos % 3600
    minutos = resto_horas_segundos // 60
    segundos = resto_horas_segundos % 60

    print(f'\n {meses} meses, {semanas} semanas, {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.')

