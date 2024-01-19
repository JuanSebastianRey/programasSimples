#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
notas=[]
suma=0
n=int(input('Ingrese la cantidad de numeros\n'))
for i in range(n):
    notas.append(float(input(f'Ingrese la nota {i+1}:\n')))
for i in range(len(notas)):
    suma+=notas[i]
print(f'Las notas {notas}')
print(f'El promedio es: {suma/n}')