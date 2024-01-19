#Área = 3.14 * radio^2
# Perímetro de un círculo = π x d
r=float(input('Ingrese el radio del circulo\n'))
if r<1:
    exit('No existe radio con ese tipo de digitos')
a=((r**2)*3.14)
p=(3.14*(r*2))
print(f'El perimetro del circulo es:{p}')
print(f'El area del circulo es:{a}')