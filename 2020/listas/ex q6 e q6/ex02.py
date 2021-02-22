v1 = [1,2,3,4,5]
v2 = [1,2,3]
# while True:
#     x = input("elm1:")
#     if x == 'fim':
#         break
#     x = int(x) 
cont = 0
for i in range(0, len(v1)):
    for j in range(0,len(v2)):
        # print(v1[i], v2[j])
        if v1[i] == v2[j]:
            cont += 1
print(f'\nPossui {cont} elementos em comum')
