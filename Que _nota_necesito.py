c1 = float(input('Ingrese nota del certamen 1:\n'))
c2 = float(input('Ingrese nota del certamen 2:\n'))
nl = float(input('Ingrese nota de laboratorio:\n'))

nc = (10*60-3*nl)/7
c3 = 3*nc-c1-c2

print(f'Necesita nota {c3} en el certamen 3')