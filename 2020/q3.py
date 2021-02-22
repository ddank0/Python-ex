a = float(input('Digite A:'))
b = float(input('Digite B:'))
c = float(input('Digite C:'))
d = float(input('Digite D:'))
n1 = int(input('Digite o primeiro intervalo:'))
n2 = int(input('Digite o segundo intervalo:'))
dx = 0
for i in range(n1,(n2+1)):
    x = a*(i**3) + b*(i**2) + c*i + d
    if x == 0:
        dx = -1
if dx == -1:
    print("\nPossui raiz")
else:
    print("\nSem ocorrencia de raiz")