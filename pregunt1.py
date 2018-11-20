import math
                            #   Entrada
try:
    x = float(input("Ingrese la coordenada x"))
    y=float(input("Ingrese la coordenada y"))

                                # Proceso

    # Estableciendo coordenadas
    fijox=0
    fijoy=0
    valor1 = x-fijox
    valor2=y-fijoy

    # Obteniendo distancia
    distancia_cuadrada = (valor1*valor1) + (valor2*valor2)
    distancia = math.sqrt(distancia_cuadrada)



                                # Salida

    print("La distancia es: "+str(distancia))
    print("La coordenada que ingreso es:"+"("+str(valor1)+","+str(valor2)+")")
except(ValueError):
    print("Los número ingresados son incorrectos")
