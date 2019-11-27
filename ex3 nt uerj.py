n1 = input('Digite sua nota:')
while n1 != 'fim':
 n1 = float(n1)
 n2 = float(input('Digite sua nota:'))
 md = (n1 + n2)/2
 if md>=7:
    print('Aprovado',md)

 elif md>=4:
    print('Em prova final',md)

 else:
     print('Reprovado',md)

 n1 = input('Digite sua nota:')
