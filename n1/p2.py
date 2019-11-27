def troca(z):

        if z.isupper() == True:
            z.lower()

        elif z.islower() == True:
            z.upper()
        return z

fr1 = ( input('algo:'))

x = troca(fr1)

print(x)


