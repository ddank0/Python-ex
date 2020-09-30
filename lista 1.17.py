geral = 0
contS = 0
contN = 0
contM = 0
sx = input('sexo:')
while sx != 'fim':
    op = input('gostou do produto:')
    geral += 1
    if op.upper() == 'SIM':
        contS += 1
    else:
        contN += 1
        if sx.upper() == 'M':
            contM += 1
    sx = input('sexo:')
print(f'''sim: {contS}
não: {contN} 
nãos masculinos: {(contM*100)/geral}%''')
    
    