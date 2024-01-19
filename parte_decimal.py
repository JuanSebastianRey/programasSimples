#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.
# Definición de la función que obtiene la parte decimal de un número real
numero_real = float(input("Ingrese un número real: "))
def obtener_parte_decimal(numero_real):
    # Se utiliza el operador de módulo (%) para obtener el residuo de la división entre el número real y 1
    parte_decimal = numero_real % 1
    
    # Si la parte decimal es igual a 0, entonces se retorna un mensaje indicando que el número no tiene parte decimal
    if parte_decimal == 0:
        return "El número no tiene parte decimal."
    
    # De lo contrario, se retorna la parte decimal del número real
    return parte_decimal
print(f"La parte decimal del número ingresado es: {obtener_parte_decimal(numero_real)}")