segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

a = segundos // 86400
resto_dias = segundos % 86400
b = resto_dias // 3600
resto_horas = resto_dias % 3600
c = resto_horas // 60
d = resto_horas % 60

print(a, "dias,", b, "horas,", c, "minutos e", d, "segundos.")