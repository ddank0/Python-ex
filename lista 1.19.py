n = int(input("digite um numero:"))
j = 0
primo = 0
cont = 0
while j < n*100:
    j += 1
    if j / 2 == 1:
        print(j)
        cont += 1
    elif j / 3 == 1:
        print(j)
        cont += 1   
    elif j / 5 == 1:
        print(j)
        cont += 1  
    elif j / 7 == 1:
        print(j)
        cont += 1  
    elif j / 11 == 1:
        print(j)
        cont += 1  
    elif j / 13 ==  1:
        print(j)
        cont += 1  
    elif j / 17 ==  1:
        print(j)
        cont += 1    
    elif j / 19 ==  1:
        print(j)
        cont += 1    
    elif j / 23 ==  1:
        print(j)
        cont += 1
    elif j % 2 == 0:
        pass
    elif j % 3 == 0:
        pass
    elif j % 5 == 0:
        pass
    elif j % 7 == 0:
        pass
    elif j % 11 == 0:
        pass 
    elif j % 13 ==  0:
        pass
    elif j % 17 ==  0:
        pass
    elif j % 19 ==  0:
        pass
    elif j % 23 ==  0:
        pass
    else:
        print(j)
        cont += 1
    if cont == n:
        break
      
    
