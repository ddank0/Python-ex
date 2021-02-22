r = float(input("Digite a taxa de juros:"))
pmt = float(input("Digite o valor das parcelas:"))
n = int(input("Digite o numero de parcelas:"))
soma  = 0
r = (r*0.01)
for i in range(1,(n+1)):
    x = pmt / (1+r) ** i
    soma += x
print('Valor do financiamento:{:10.2f}'.format(soma))

# N entendi a questão, acho q é isso kk
