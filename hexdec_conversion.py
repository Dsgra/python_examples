'''
Convertir hexadecimales va a ser la siguiente tarea que vamos a definir para comprobar esta libreria y su potencial a la hora de seguir desarrollando mi unidad
'''
hx = int(input("Introduce el valor numerico que deseas convertir en hexadecimal"))

# hex() function
print("El valor hexadecimal del numero introducido es: " + hex(hx))

# hex(ord('a')

print("la forma hexadecimal de la letra a " " ascii valor  es: " + hex(ord('a')))

print("La forma hexadecimal del decimal 3.9 es " + float.hex(3.9))

# Comenzamos otro pedazo de codigo para poder posibillitar al usuario a introducir sus propios valores

number = int(input("Introduce el numero con base 10\n que desee:"))

# Aqui declaramos las opciones puestas al alcance del usuario
print("a. Decimal to Hexadecimal ")
print("b. Decimal to Octal ")
print("c. Decimal to Binary ")

# Tomando el input del usuario
print("Introduce tu seleccion:- ")
choice = input()

# Ejecutar una variable elegida. La forma hexadecimal es set en 0
if choice is 'a':
    # lstrip ayuda para remover '0x' de la izquierda
    # rstrip ayuda a remover 'L' de la derecha
    # L sirve para representar un numero largo
    print("La Forma Hexadecimal de : " + str(number) + " is " + hex(number).lstrip("0x").rstrip("L"))
    
if choice is 'b':
    # Representacion Octal se realiza 
    # Anadiendo el prefijo '0x'
    print("La Forma Octal de : " + str(number) + " is " + oct(number).lstrip("0o").rstrip("L"))
    
if choice is 'c':
    # La representacion binaria se realiza
    # anadiendo el prefijo '0b'
    print("La Forma Binaria de " + str(number) + " is " +bin(number).lstrip("0b").rstrip("L"))


