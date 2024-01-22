Algoritmo sin_titulo
	definir r,a,p como real
	Escribir 'Ingrese el radio del circulo'
	leer r
	si r<1 Entonces
		Escribir 'No existe radio con ese tipo de digitos'
	FinSi
	a=((r^2)*3.14)
	p=(3.14*(r*2))
	Escribir 'El perimetro del circulo es:',p
	Escribir 'El area del circulo es:',a
FinAlgoritmo
