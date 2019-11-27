cadeia = input('entre com uma cadeia:')
soma = 0
for i in range (0,len(cadeia)):
    soma  += ord(cadeia[i])
print('SOMA:',soma)