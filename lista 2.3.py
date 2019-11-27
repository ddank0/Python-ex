def vogal(z):
    v = True
    if z == 'A':
        return v
    if z == 'E':
        return v
    if z == 'I':
        return v
    if z == 'O':
        return v
    if z == 'U':
        return v
    else:
        return not v
fr = input('Digite uma frase:')
vog = []
vz = []
resto = []
for i in fr:
    print(i)
    if vogal(i.upper())== True:
        vog.append(i)
    elif i.isspace() == True:
        vz.append(i)
    else:
        resto.append(i)
print('vogais:',len(vog))
print('espaço:',len(vz))
print('resto:',len(resto))