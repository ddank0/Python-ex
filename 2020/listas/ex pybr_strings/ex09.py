n = input("Digite o CPF:")
n = n.replace(".","")
n = n.replace("-","")
if len(n) != 11:
    print("ERROR")
elif n.isdigit() == True:
    print("CPF válido")
else:
    print("ERROR")
