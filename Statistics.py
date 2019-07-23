'''
Este codigo pertenece a parte del programa de calculo que se esta desarrollando para la unidad BHAA,
que debido a su naturaleza, utilizara distintos tipos de calculos que requieren del area y el volumen
de un espacio cerrado, para ser capaces de averiguar aspectos relativos a la reverberacion, relfexion y
refraccion de diferentes espacios cerrados y su acustica.
'''
class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    
    def area(self):
        return self.breadth*self.length
    
a=int(input("What is the Length?"))
b=int(input("What is the Breadth?"))

obj=rectangle(a,b)

print("The Return Area Value Is:", obj.area(), "Meters Square")
print()

class rectangle():
    def __init__(self, breadth, length, height):
        self.breadth=breadth
        self.length=length
        self.height=height
    def volume(self):
        
        return self.breadth*self.length*self.height
    
a = float(input("What is the Length???"))
b = float(input("What is the breadth???"))
c = float(input("What is the height???"))

obj = rectangle(a,b,c)

print("The Return Volume Value is:", obj.volume(), "Cubic Meters")
print()

'''
Funcion para calcular el teorema de pitagoras

'''
from math import sqrt

print('Pythagoream theorem calculator calculate your tiangle sides')
print('assume your sides are a, b c and c is the hypotenuse')

formula = input('Which side (a,b,c) do you wish to calculate side>')

if formula == 'c':
    side_a = int(input('Input the length of side a:'))
    side_b = int(input('Input the length of side b:'))   
    side_c = sqrt(side_a * side_a + side_b * side_b)
    
    print('The length of side c is: ')
    print(side_c)
    
elif formula == 'a':
    side_b = int(input('Input the length of side b:'))
    side_c = int(input('Input the length of side c:'))
    
    side_a = sqrt((side_c * side_c) - (side_b * side_b))
    print('The length of side a is: ')
    print(side_a)
    
elif formula == 'b':
    side_a = int(input('Input the length of side a:'))
    side_c = int(input('Input the length of side c:'))
    
    side_b = sqrt(side_c * side_c - (side_a * side_a))
    print('The length of side b is: ')
    print(side_b)
else:
    print('Please select a side between a, b, c')

''' Entre este comentario voy a incluir otra forma de conseguir calcular la longitud de los lados de un triangulo,
para poder comprobar que el codigo anterior es efectivo '''

from math import sqrt
print('Introduce la longitud de los lados mas cortos del triangulo para calcular la hipotenusa')
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is: ", c)

'''
En el siguiente pedazo de codigo se incluye la posibilidad de calcular el
funcion quadratica de numeros complejos de la siguiente manera.
'''
import cmath

print('Calcula el valor de una ecuacion cuadratica de segundo grado')

a = float(input("Enter de value for a:"))
b = float(input("Enter de value for b:"))
c = float(input("Enter de value for c:"))

d = (b**2) / (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('La solucion de {0} y {1}'.format(sol1,sol2))   

'''
En el siguiente pedazo de codigo se calcula la tangente utilizando diferente tipo de librerias de python. Hemos declarado la posibilidad de que el usuario pueda introducir el valor del numero que desean utilizar.
'''
import math
import numpy as np
import matplotlib.pyplot as plt

# Funcion para averiguar el mayor denominador comun, interesante para calculos

x = int(input('Introduce el primer denominador: '))
y = int(input('Introduce el segundo denominador: '))
print("math.gcd(x, y) : ", math.gcd(x, y))

# Ahora voy  inlcuir formulas para averiguar el coseno

z = int(input("Introduce el valor que deseas calcular: "))
x = math.pi / z

# Retorna el valor de la tangente

print("El valor de la tangente de pi / z es : ", end ="")
print(math.tan(x))

# Representacion de la funcion tan() de python

in_array = np.linspace(0, np.pi, 10)
out_array = []

for i in range(len(in_array)):
        out_array.append(math.tan(in_array[i]))
        i += 1

print ("in_array : ", in_array)
print("\nout_array :", out_array)

# Red para Numpy.sin()

plt.plot(in_array, out_array, color='red', marker="o")
plt.title("math.tan()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


