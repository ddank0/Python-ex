vet = []
for i in range(0,8):
    vet.append(input('digite:'))
print(vet)
for i in range(0,4):
    aux=vet[i]
    vet[i]=vet[i+4]
    vet[i+4]=aux
print('Vetor trocado:',vet)

