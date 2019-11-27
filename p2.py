
def troca(z):
    lita = []
    for i in z:
        if i.isupper() == True:
            lita.append(i.lower())
        elif i.islower() == True:
            lita.append(i.upper())  
        else:
            lita.append('')    
    print(lita)

fr1 = ( input('algo:'))
x = troca(fr1)


