# a1 = input("digite:")
# a2 = ""
# for i in range((len(a1)-1),-1,-1):
#   print(i)
#   a2 += a1[i]
# print(a2)
import random
x  = random.randint(10000,999999)
x = str(x)
z = "0"
if len(x) == 5:
  for i in x:
    z += i
print(z)
