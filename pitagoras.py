#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b
#de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
#del triangulo, dado por el teorema de Pitágoras: c2=a2+b2.
import math
a=float(input('Ingrse el valor del primer cateto:\n'))
b=float(input('Ingrese el valor del segundo cateto:\n'))
if a<1 or b<1:
    exit('No existen medidas negativas en longitudes sobre un triangulo')
c2=(math.pow(a,2)+math.pow(b,2))
c = math.sqrt(c2)
print(f'La hipotenusa del triangulo es: {c}')