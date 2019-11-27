import math
e = 0
x = int(input('entre com x:'))
y = int(input('entre com y:'))
for i in range (1,51):
     e = e +(((x + math.sqrt(y+2))/3)+(i**2-y**5))
print('e:',e)