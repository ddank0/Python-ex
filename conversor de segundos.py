times = int(input('Tempo em segundos:'))
hora = times // 3600
minuto = (times % 3600) // 60
segundos = (times % 3600) % 60

print(hora,'h',minuto,'min',segundos,'s')
