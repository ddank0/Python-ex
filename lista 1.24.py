n = int(input("digite um numero:"))
primo = 0
cont2 = 0
t1 = 0
t2 = 1
t3 = 0
while True:
    cont = 0
    t3 = t1 + t2
    for i in range(1,(t3+1)):
        if t3 % i == 0:
            cont += 1
    if cont == 2:
        print(t3)
        cont2 += 1
    t1 = t2
    t2 = t3      
    if cont2 == n:
        break
    