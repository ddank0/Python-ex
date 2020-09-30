n = 0
cont = 0
while cont < 4:
    n += 1
    soma = 0
    for i in range(1,(n+1)):
        if n % i == 0 and i != n:
            soma += i
    if soma == n:
        print(n)
        cont += 1

    
 