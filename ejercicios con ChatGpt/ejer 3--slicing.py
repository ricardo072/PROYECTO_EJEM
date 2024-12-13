'''Ejercicio 3: Saltos en el slicing
Dada la cadena:

Extrae cada tercera letra desde el inicio.
Invierte la cadena utilizando slicing.
Extrae las letras desde la posición 5 hasta la 20, tomando solo cada segunda letra.'''

alfabeto = "abcdefghijklmnopqrstuvwxyz"
ejem1=alfabeto[0::3]
ejem2=alfabeto[::-1]
ejem3=alfabeto[5:20:2]

print('ejer 1---- ',ejem1,'ejem 2------ ',ejem2, 'ejer3-------- ',ejem3)