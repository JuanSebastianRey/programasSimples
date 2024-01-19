# Escriba un programa que pida al usuario un entero de tres dígitos,
# y entregue el número con los dígitos en orden inverso:

number = int(input('Ingrese numero:\n'))
i_n = 0
while number>0:
    i_n *=10
    i_n += (number%10)
    i_n//10
print(i_n)