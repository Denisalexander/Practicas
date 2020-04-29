# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:32:24 2020

@author: Denis
"""

print("================================")
print(" Bienvenidos a mi cifrado César")
print("================================")

abecedario= " abcdefghijklmnñopqrstuvwxyz "

texto_claro= input("Introduce una frase para cifrarla, esta pasara a minúsculas: ")
clave= int(input("Introduce un número para cifrar(Un número del 1 al 27):"))

#Mejora: convierte todo el texto en minúsculas antes de cifrarlo.

texto_claro_min= texto_claro.lower()

#Mejora: convierte todo el texto en minúsculas antes de cifrarlo.


texto_cifrado=""


for letra in texto_claro_min:
    nueva_posicion= abecedario.find(letra)+ clave
    letra_cifrada= int(nueva_posicion)%len(abecedario)
    texto_cifrado= texto_cifrado+str(abecedario[letra_cifrada])



print ("El mensaje cifrado es:" ,texto_cifrado)

texto_descifrado=""
for letra in texto_cifrado:
    nueva_posicion= abecedario.find(letra)-clave
    letra_cifrada= int(nueva_posicion)%len(abecedario)
    texto_descifrado= texto_descifrado+str(abecedario[letra_cifrada])
print ("El mensaje descifrado es: " ,texto_descifrado)