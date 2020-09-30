t1 = 0
t2 = 1
cont = 0
n = int(input('numero:'))
for i in range(1,(n+1)):
    # print(t1)
    x = t1 + t2
    t1 = t2
    t2 = x
    if t1 % i == 0:
        cont += 1
if cont == 2:
    print(t1)     