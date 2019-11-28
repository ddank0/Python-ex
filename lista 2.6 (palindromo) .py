palindromo = False
fr1 = input("digite:")
invert = ''
for i in range(len(fr1)-1,-1,-1):
    invert += fr1[i]
    if invert == fr1:
        palindromo = True
print(palindromo)
