v1 = [10,20,30,40]
v2 = ['a','b','c','d']
x = []
if len(v1) == len(v2):
    for i in range(0,len(v1)):
        x.append(v1[i])
        x.append(v2[i])
    print(f'\n{x}')
else:
    print(f'\nERROR')