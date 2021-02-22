try:
    l1 = int(input('lado1:'))
except ValueError:
    print("Tente novamente (insira apenas numeros)")
    l1 = int(input('lado1:'))
if l1 < 0:
    print("ERROR")
while l1 > 0:
    try:
        l2 = int(input('lado2:'))
        l3 = int(input('lado3:'))
    except ValueError:
        print("Tente novamente (insira apenas numeros)")
        l2 = int(input('lado2:'))
        l3 = int(input('lado3:'))

    x = (l2**2) + (l3**2)
    y = (l1**2) + (l3**2)
    z = (l1**2) + (l2**2)

    if l1 < 0 or l2 < 0 or l3 < 0:
        print("Não é um triângulo")  

    elif l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
        if l1 == l2 and l2 == l3:
            print("triângulo equilátero")
        elif l1 == l2 or l2 == l3 or l3 == l1:
            print("triângulo isósceles")
        elif l1**2 == x or l2**2 == y or l3**2 == z:
            print("triângulo retângulo")
        else:
            print("triângulo escaleno não retangulo")

    else:
        print("Não é um triangulo")
    try:
        l1 = int(input('lado1:'))
    except ValueError:
        print("Tente novamente (insira apenas numeros)")
        l1 = int(input('lado1:'))
