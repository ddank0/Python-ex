n = int(input("digite um numero:"))
j = 0
primo = 0
cont2 = 0
while j < n*1000:
    cont = 0
    j += 1
    for i in range(1,(j+1)):
        if j % i == 0:
            cont += 1
    if cont == 2:
        print(j)
        cont2 += 1
       
    if cont2 == n:
        break

      
    
