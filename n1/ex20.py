vet1 = []
vet2 = []
n = int(input('N:'))
while n >= 0:
    vet1.append(n)
    n = int(input('N:'))
print('v1:',vet1)

n = int(input('N:'))
while n >= 0:
    vet2.append(n)
    n = int(input('N:'))
print('vt2:',vet2)

for i in range(0,len(vet1)):
    for j in range(0,len(vet2)):
        if vet1[i] == vet2[j]:
            print('int:',vet1[i])
