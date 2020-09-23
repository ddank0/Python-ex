contS = 0
contN = 0
geral = 0

x = input('Está satisfeito:')
while x != 'F':
    geral += 1
    if x.upper() == 'S':
        contS += 1
    else:
        contN += 1
    x = input('Está satisfeito:')

print(f'''sim: {(contS*100)/geral}%
não: {(contN*100)/geral}%''')
    