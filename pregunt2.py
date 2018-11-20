                            # Entrada

matriz=[]
def menor_arreglo(matriz):
    a=matriz[0]
    menor = 0 
    for i in matriz:
        if(i<=a):
            menor=i
        return menor


                            # Proceso
while len(matriz)<5:
    a = int(input("Ingrese un número:"))
    matriz.append(a)
print(matriz)
print(menor_arreglo(matriz))





         
      