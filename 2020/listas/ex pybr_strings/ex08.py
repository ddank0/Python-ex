x = input("digite:")
y = ""
print(f"\n{x}")
for i in range(len(x)-1,-1,-1):
    y += x[i]
print(f"\n{y}")
y = y.replace(" ","")
if x == y:
    print("\nÉ um palindromo")
else:
    print("\nNão é palindromo")