numeros = [23,-14, 0, 0, 21, -9, -5, 34, 89]
Contceros = 0
Contpos = 0
Contneg = 0

for numero in numeros:  
    if (numero == 0):
        Contceros +=1
    elif (numero > 0):  
        Contpos +=1
    else:
        Contneg +=1

print("Ceros ", Contceros)
print("Positivos ", Contpos)
print("Negativos", Contneg)

  
   
