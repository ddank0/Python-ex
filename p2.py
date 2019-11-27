
f = open('p2.txt',"w")
fr1 = ( input('algo:'))
fr2 = ( input('dnv:'))
f.write(fr1+"\n")
f.write(fr2)
f.close()
x = open('p2.txt','r')
zet = open('p2f.txt',"w")
for i in x:
    if i.isupper() == True:
        zet.write(i.lower())
    elif i.islower() == True:
        zet.write(i.upper())
    elif i.isspace() == True:
        pass
    elif i.isalpha() == False:
        zet.write('%')
x.close()
zet.close()
