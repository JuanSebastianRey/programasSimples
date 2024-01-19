import math
TH = float(input('Temperatura original del huevo:\n')) #TEmperatura del huevo
TE = 100#Temperatura del agua en ebullicion
M = 47#Masa del huevo
P = 1.038#Densidad del huevo
C = 3.7#Capacidad calorica
K = 0.0054#Conductividad termica
dividendo=(math.pow(M,(2/3))) * (C*(math.pow(P,(1/3))))
divisor=(K*(math.pow(math.pi,2)))*math.pow((4*math.pi)/3,(2/3))
resultado=dividendo/divisor
resultado2=math.log(0.76*(((TH-TE))/(70-TE)))
segundos=resultado*resultado2
minutos=round((resultado*resultado2)/60)
print(f'El tiempo maximo para prepararlo a la copa en segundos es: {round(segundos)}')
print(f'El tiempo maximo para prepararlo a la copa en minutos es: {minutos}')