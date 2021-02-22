v1 = [1,1,6,6,7,7,7,7,1,1,1]
cont = 1
cont2 = []
x = []
for i in range(0,len(v1)):
    y = v1[i]
    if x == y:
        cont += 1 
    if x != y:
        cont2.append(cont)
        cont = 1
    x = v1[i]
cont2.append(cont)
cont2.sort(reverse=True)
print(f"\nt = {cont2[0]}")
print(cont2)