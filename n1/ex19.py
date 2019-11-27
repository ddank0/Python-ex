vtnum = []
num = (input('N:'))
while num.upper() != 'FIM':
    vtnum.append(num)
    num = (input('N:'))
n = (input('nº buscado:'))
pos = []
cont = 0
for i in range(0,len(vtnum)):
    if n == vtnum[i]:
        cont = cont + 1
    if n == vtnum[i]:
        pos.append(i)
if len(pos) >= 1:
    print('Pos:',pos)
else:
    print ('Vetor vazio')

print('qt:',cont)
