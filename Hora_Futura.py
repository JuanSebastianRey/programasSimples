t=float (input('Ingrese la hora actual:·\n'))
ch=int(input('Ingrese las horas que va a trabajar:\n'))
horas=int(t+ch)%2400
print(f'En {ch}, el reloj marcara a las {horas}')