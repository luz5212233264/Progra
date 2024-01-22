import math

def resolver_ecuacion_cuadratica(a, b, c):
    # Calcular el discriminante
    discriminante = b**2 - 4*a*c

    # Verificar si hay soluciones reales
    if discriminante >= 0:
        # Calcular las soluciones utilizando la fórmula cuadrática
        solucion1 = (-b + math.sqrt(discriminante)) / (2*a)
        solucion2 = (-b - math.sqrt(discriminante)) / (2*a)

        # Imprimir las soluciones
        print("Solución 1:", solucion1)
        print("Solución 2:", solucion2)
    else:
        print("La ecuación cuadrática no tiene soluciones reales.")

# Pedir al usuario que ingrese los coeficientes
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

# Resolver la ecuación cuadrática
resolver_ecuacion_cuadratica(a, b, c)

