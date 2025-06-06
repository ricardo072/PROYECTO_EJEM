'''Intercambia valores: Crea dos variables, x y y, con los valores 5 y 10.
Escribe un programa que intercambie los valores entre las variables, de manera que x valga 10 y y valga 5, e imprime los resultados.'''
x=5
y=10
#apartir de aqui voy a cambiar los valores
g=x

x=y
y=g
print(x,y)

'''Cálculo del promedio de tres números
Escribe un programa que haga lo siguiente:

Define tres variables con los números a = 8, b = 12, y c = 20.
Calcula el promedio de estos tres números.'''

a,b,c=8,12,20
print((a+b+c)/3)



'''Escribe un programa que haga lo siguiente:


Define una variable llamada segundos_totales, con un número entero que represente una cantidad de segundos (por ejemplo, segundos_totales = 7384).

Convierte este número de segundos en:

Horas
Minutos
Segundos restantes.
Imprime el resultado en el formato:
"7384 segundos son equivalentes a 2 horas, 3 minutos y 4 segundos."'''

segundos_totales=7384
horas=segundos_totales//3600

minutos_restantes=(segundos_totales % 3600)//60
segundos_restantes=segundos_totales%60


print(segundos_totales,' segundos son equivalentes a ',horas, 'horas', minutos_restantes,' minutos con',segundos_restantes,'segundos')
