n = int(input('Digite um numero:'))
b = int(input('Base desejada:'))
total = ""
if b == 0 or b == 1:    
    print("ERROR")
    total = "error"
elif n != 0:  
    while n > 0:
        x = n % b
        n = n // b
        total = str(x) + total
else:
    total = "0"
print("resultado: {:10s}".format(total))