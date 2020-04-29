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
for bucle in range(edad -1):
    print("Que no cumple " + str(bucle +1))
print ("¡Que si cumple " + str(edad) + "!\n")

#datos guardados en diccionario
print ("DATOS RECOGIDOS\n")
datos = {
        "datos_nombre":nombre,
        "datos_nacimiento":nacimiento,
        "datos_edad":edad}

for bucledatos in datos.values():
    print (bucledatos)

import time
time.sleep(17)