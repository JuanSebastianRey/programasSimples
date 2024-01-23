# Escriba un programa que pida al usuario un entero de tres dígitos,
# y entregue el número con los dígitos en orden inverso:

numero = int(input("Ingrese un número de tres dígitos: "))

while numero < 100 or numero > 999:
   print("El número debe tener exactamente tres dígitos.")
   numero = int(input("Ingrese un número de tres dígitos: "))

d1 = numero // 100 
d2 = (numero % 100) // 10 
d3 = numero % 10 

numero_invertido = d3 * 100 + d2 * 10 + d1

print("El número invertido es:", numero_invertido)