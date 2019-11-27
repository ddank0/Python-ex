nota=[]
nota_nova=int(input('nota = '))
while (nota_nova >= 0):
    flag=1
    while(flag==1):
        cont=0
        for j in range(0,len(nota)):
            if (nota[j] != nota_nova):
                cont = cont+1
            if(cont==len(nota)):
                nota.append(nota_nova)
                flag=0
        nota_nova = int(input('nota = '))
print(nota)