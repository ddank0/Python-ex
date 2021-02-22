y = input('número:')
x = int(input('base:'))
if x >= 2:
    num = int(y, x)
    print('resultado: {:d}'.format(num))
else:
    print('error')