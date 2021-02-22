v1 = []
v2 = []
for j in range(0,5):
    num = int(input("digite um número:"))
    v1.append(num)
for i in v1:
    # print(i)
    if i%2 != 0:
        x = i*3
        v2.append(x)
    if i%2 == 0:
        x = i*2
        v2.append(x)
print(v2)