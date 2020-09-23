cont0 = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0 
nulos = 0
geral = 0
vt = int(input('digite seu voto:'))
while True:
    geral += 1
    if vt == 0:
        cont0 += 1
    elif vt == 1:
        cont1 += 1        
    elif vt == 2:
        cont2 += 1
    elif vt == 3:
        cont3 += 1
    elif vt == 4:
        cont4 += 1
    else:
        nulos +=1
    if geral == 20000:
        break
    vt = int(input('digite seu voto:'))
    
print(f'''Votos em branco: {cont0}
Votos nulos: {nulos}
João da Silva: {cont1}
José Ramalho: {cont2}
Maria Mattos: {cont3}
Pedro Américo: {cont4}''')