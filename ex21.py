vet = []
n = input('A = adicionar / R = remover / I = imprimir / F = sair:')
while n.upper() != 'F':
    if n.upper() == 'A':
        any = input("elemento:")
        vet.append(any)
    elif n.upper() == 'R':
        vet.pop()
    elif n.upper() == 'I':
        print(vet)
    else:
        print('opção invalida')
    n = input('A = adicionar / R = remover / I = imprimir / F = sair:')