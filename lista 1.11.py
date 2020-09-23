n = int(input('digite um número:'))
soma = 0
if n < 0:
    print("numero invalido")
else:
    for i in range(0,(n+1)):
        if i%2 != 0:
            soma += i
print(soma)
