#Ejercicio 1: Acceso básico a partes de una cadena
'''
1 =Extrae la palabra "slicing".
2= Extrae las primeras 10 letras de la cadena.
3- Extrae las últimas 6 letras.
'''
frase = "Aprendiendo slicing en Python"
ejer1=frase.find('slicing')
ejer1=frase[ejer1:19]
ejer2=frase[:10]
ejer3=frase[6:]
print('1----',ejer1,'2-----',ejer2,'3------',ejer3)



