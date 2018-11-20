def menor_valor(matriz,mayorvalor):
    valor=mayorvalor
    for i in matriz:
        if(i<=valor):
            valor=i
    print("El menor valor es:"+str(valor))                            
                            
                            
                            # Entrada

matriz=[]



                            # Proceso
while len(matriz)<5:
    a = int(input("Ingrese un número:"))
    matriz.append(a)
b=max(matriz)

                        # Salida
 
menor_valor(matriz,b)











         
      