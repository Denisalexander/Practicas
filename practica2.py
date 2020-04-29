# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:04:31 2020

@author: Denis
"""
print ("============================")
print ("BIENVENIDO A EMPAREJANDO.COM")
print ("============================\n")
print ("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal")

nombre= input("Tu nombre:\n")
nacimiento= int(input("Año de nacimineto:\n"))
pregunta= input("¿Te gusta taburete?\n")

edad= 2020  -nacimiento

print ("\nHola," + " " + nombre + "." + " Si no me equivoco, tienes " + str(edad)  + " años.\n")

if pregunta=="si":
    print("OK Boomer, lo tuyo va a ser un caso dificil\n")
elif pregunta==("no"):
    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo\n")
else:
    print("Debes responder con si o no\n")
    
#bucle 
edadbucle= edad -2
num=0
suma=1
while (num<=edadbucle):
    num=num+suma
    
    
    print ("Que no cumpla " + str(num))

print ("¡Que si cumpla " + str(edad) + "!")

import time
time.sleep(10)