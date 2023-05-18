lista = []
total=0


for i in range(5):  
    numero=int(input("ingrese un numero:"))
    lista.append(numero)
    
print(lista)

for numero in lista:
    total =total + numero

print (total)  

promedio = total / len(lista)

print(promedio)


