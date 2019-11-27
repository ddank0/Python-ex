n1 = input('Digite um valor:')
n2 = input('Digite um valot:')
s = n1 + n2
if n1  == '' :
    print('erro')
if n1 != '':
    n1 = int(n1)
#print('soma entre',n1,'e',n2,'vale',s)
print ('A soma entre {0} e {1} vale: {2}'.format(n1,n2,s))
print(n1)