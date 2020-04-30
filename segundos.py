segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos = int(segundos_str)

dias = segundos // 86400
sobraDosDias = segundos % 86400
horas = sobraDosDias // 3600
sobraDasHoras = sobraDosDias % 3600
minutos = sobraDasHoras // 60
segundosFinal = sobraDasHoras % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundosFinal, "segundos.")
