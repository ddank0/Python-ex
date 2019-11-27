cadeia = input('entre com uma cadeia:')
while cadeia != 'fim':
    contA = 0
    contN = 0
    contO = 0
    for i in range (0,len(cadeia)):
        if cadeia [i].isalpha():
            contA += 1
        elif cadeia[i].isdigit():
            contN += 1
        else:
            contO += 1
    print('LETRAS:',contA,'NUMEROS:',contN,'OUTROS:',contO)
    cadeia = input('entre com uma cadeia:')