cont_p = 0
cont_np = 0
n = int(input("Digite um numero:"))
while n >= 0:
    soma = 0
    for i in range(1,(n+1)):
        if  n % i == 0 and i != n:
            soma += i
    if soma == n:
        cont_p += 1
    else:
        cont_np += 1
    n = int(input("digite um número:"))
print("Quantidade de números perfeitos: {:d}".format(cont_p))
print("Quantidade de números não perfeitos: {:d}".format(cont_np))

