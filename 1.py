# -*- coding: utf-8 -*-
"""clases y objetos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15vGxuIsan0xQT0Gp4czLpqKJeqieT4at

codigo #1

parrafo 1

La siguiente clase es sobre los calculos basicos de un circulo en r2 conociendo con anterioridad el radio y en caso de querer calcular la cuerda el angulo desde el centro del circulo, y con esto generar los valores del area,diametro,cuerda y perimetro.

parrafo 2

el codigo podria ser modificado para que se pueda calcular esta misma informacion en r3, pero le veo mas utilidad mas puntualmente para calcular las dimensiones de los planetas, en el futuro cuando los humanos puedan viajar por el espacio y pueda ir documentando las dimensiones de los nuevos planetas descubiertos para hacer colonias en los planetas con mayores dimensiones.
"""

import math
class Circulo:
     pi = 3.14159                     
     def __init__(self, radio,angulo):
         self.radio = radio
         self.angulo = angulo
     def area(self):
         return Circulo.pi * self.radio ** 2
     def diametro(self):   
         return self.radio*2
     def perimetro(self):
         return self.radio*Circulo.pi*2 
     def cuerda(self):
         return 2*self.radio*(math.sin(self.angulo*(Circulo.pi/180)/2))

c1 = Circulo(1,90)
print("el area del circulo 1 es:", c1.area(), "m^2")
print("el diametro del circulo 1 es:", c1.diametro(),"m")
print("perimetro", c1.perimetro(),"m")
print("cuerda",c1.cuerda())

"""codigo #2

parrafo 1

el siguiente codigo representa una tarjeta del sitp para saber que saldo tiene, ya sea que se haya recargado, se haya pagado el pasaje o ambas de las anteriores cosas, usando un identificador de tarjeta y conociendo el valor inicial que tiene la tarjeta.

parrafo 2

el codigo se puede implementar en el futuro con microchips especiales que estan dentro del cuerpo para llevar el dinero, y pagar directamente, ya sea el pasaje o cualquier objeto en cualquier tienda, recargar entre cuentas, recargar desde dinero almacenado en el banco para no correr el riesgo de cargar grandes cantidades.
"""

class Tarjetasitp:
    def __init__(self, id, cantidad = 0):
        self.id = id
        self.saldo = cantidad
        return
    def mostrar_saldo(self):
        print('El saldo es ${:.2f}'.format(self.saldo))
        return
    def pagarpasaje(self, cantidad):
        self.saldo -= cantidad
        return
    def recargar(self,cantidad):
        self.saldo += cantidad

t1 = Tarjetasitp('1563587', 1000)
t1.pagarpasaje(2600)
t1.recargar(3000)
t1.mostrar_saldo()