x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)
'''
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
'''
import random
print ('este es mi primer ramdon ',random.randrange(1,3))

#  choice()        Devolver un elemento aleatorio de una lista:

lista1=['piedra','papel','tijera']
print('ejemplo de choice ',random.choice(lista1))


'''sample() método devuelve una lista con un número especificado de elementos seleccionados aleatoriamente de una secuencia.

Nota: Este método no cambia la secuencia original.

Nota: El número especificado (k=2) no puede ser más largo que la longitud de la secuencia original.'''

acortar_y_random=random.sample(lista1,k=2)
print('ejemplo de sample ',acortar_y_random)

# el random.random devuelve un numero aleatoreo entre 0.0 y 1.0 y siempre es flotad
rando=random.random()

# el random.uniform devuelve un numero fload aleatoreo entre un rango dado (33,55) y siempre es fload
ejem_uniform=random.uniform(22,33)
print('ejem de uniform ',ejem_uniform)

#Devuelva un número aleatorio entre un rango y el mode  lo más probable que salga ejem 1 ,4 es el rango y ,2 es el mode =resul 2.88
# y todos los resultados son fload

ej_triangular=random.triangular(1,5,2)
print('ejem de triangular  ',ej_triangular)
