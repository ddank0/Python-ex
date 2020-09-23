n1 = int(input('Primeiro termo:'))
n2 = int(input('razão:'))
term = int(input('quantidade de termos:'))
soma = n1
print(n1)
for i in range(0,term):
    if soma  == n1:
        soma = n1 + n2
        print(soma)
    else:
        soma += n2
        print (soma)

