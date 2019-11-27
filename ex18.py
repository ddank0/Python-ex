nt = []
npar = []
nimp = []
soma = 0
media = 0
n = int(input('1º número:'))

while n!=0:
    nt.append(n)
    n = int(input('1º número:'))

for i in range(0,len(nt)):

        if nt[i]%2 == 0:
            npar.append(nt[i])

        if nt[i]%2 !=0:
            nimp.append(nt[i])
            soma = nt[i] + soma
            media = soma/len(nimp)

print('total:',nt)
print('qt par:',len(npar))
print('media imp:',media)



