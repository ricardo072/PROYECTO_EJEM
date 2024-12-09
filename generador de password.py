# esta sera mi primera obra y es un generador de password
import random
numeros=['1','2','3','4','5','6','7','8','9','0']
letras=['a','s','d','f','g','h','j','k','q','w','w','r','t','y','u','i','o']
simbolos=['!','@','#','$','$','%','^','&','*','(',')']
unir=numeros+letras+simbolos
longitud=8
password=random.sample(unir,k=longitud)
password=''.join(password)
print(password)


