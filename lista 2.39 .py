vet = []
vet2 = []
with open("entrada.txt","w") as entra1:
    x = input("algo:")
    entra1.write(x)
with open("entrada.txt","r") as entra2:
    for i in entra2:  
        
        i.split() 
        print(i)

        if i.isspace == True:
            pass
        if i.isalpha == False:
            pass
        if i.isnumeric == True:
            pass
        else:
            vet.append(i.split())

print(vet)
print(len(vet))
    

        

    

    

    
