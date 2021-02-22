testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
primeiro = 0
ultimo = len(testlist) - 1
achou = False
item = int(input('numero procurado:'))
while primeiro <= ultimo and not achou:
    x = (primeiro + ultimo)//2
    if testlist[x] == item:
        achou = True
    else:
        if item < testlist[x]:
            ultimo = x - 1
        else:
            primeiro = x + 1
print(achou)