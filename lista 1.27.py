a = float(input('digite A:'))
b = float(input('digite B:'))
c = float(input('digite C:'))
d = float(input('digite D:'))
dx = 0
for i in range(-1000,1000):
    x = a * (i ** 3) + b * (i ** 2) + c * i + d
    if x < 0:
        dx = -1
if dx == -1:
    print('possui raiz')
else:
    print('sem ocorrencia de raiz')