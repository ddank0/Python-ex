quant = int(input("Quantidade de numeros:"))
cont_p = 0
cont_np = 0
cont = 0
n = int(input("Digite um numero:"))
while quant != cont:
    cont += 1
    soma = 0
    for i in range(1,(n+1)):
        if  n % i == 0 and i != n:
            soma += i
    if soma == n:
        cont_p += 1
    else:
        cont_np += 1
    n = int(input("Digite um numero:"))
print("Quantidade de números perfeitos: {:1d}".format(cont_p))
print("Quantidade de números não perfeitos: {:1d}".format(cont_np))
