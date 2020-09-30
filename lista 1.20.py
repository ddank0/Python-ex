n = int(input("digite um número:"))
soma = 0
for i in range(1,(n+1)):
    if  n % i == 0 and i != n:
        soma += i
if soma == n:
    print('numero perfeito')
else:
    print('numero não perfeito')