l1 = float(input('lado1:'))
l2 = float(input('lado2:'))
l3 = float(input('lado3:'))
p = 0
a = 0
if l1 <= 0 or l2 <= 0 or l3 <=0:
    print('dados invalidos')
else:
    p = (l1+l2+l3)/2
    a =(p*(p-l1)*(p-l2)*(p-l3))**(1/2)
    print('área:',a)
