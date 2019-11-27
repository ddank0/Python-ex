soma = 0
cont = 0
nota =[ ]
for i in range(0,5):
    nota.append(float(input("Nota:")))
    soma = nota[i] + soma
    media = soma/5
for j in range(0,5):
        if nota[j] >= media:
            cont+=1
            print(nota[j])
print('media:',media)
print('qut:',cont)




