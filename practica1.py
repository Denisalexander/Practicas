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

print ("hola," + " " + nombre + "." + "Si no me equivoco, tienes " + str(edad)  + " años.")

if pregunta=="si":
    print("OK Boomer, lo tuyo va a ser un caso dificil")
elif pregunta==("no"):
    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo")
else:
    print("debes responder con si o no")
    
import time
time.sleep(5)