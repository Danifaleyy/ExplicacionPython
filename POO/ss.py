#Importamos librerias
import matplotlib.pyplot as plt #libreria para graficar
import math #libreria para operaciones avanzadas de matematicas
from tabulate import tabulate #Libreria para hacer tablas
#Declaracion de variables y listas
#Velocidad
v=0.0
#tiempo
t=1
x=0
#gravedad
g=9.8
vA=0.0
#Listas
ListaX=[]
Listay=[]
tabla=[]
#Pedir los datos
#m = masa
m=float(input("Peso del paracaidista:"))
#c=coeficiente
c=float(input("Coeficiente de resistencia del aire:"))
#Durante este ciclo se hara el procedimiento para la solucion del problema
while True:
    #Insertamos los datos de x y v hacia sus respectivas listas 
    tabla.append([x,v])
    ListaX.append(x)
    Listay.append(v)
    vA=v
    v=((g*m)/c)*(1-math.exp(-(c/m)*t))#Utilizacion de la formula
    x=x+1
    t=t+1
    if(v==vA):#Condicion en la cual compara la velocidad actual con la velocidad anterior para ver si son constantes
        break
#Utilizamos tabulate para que imprima los datos en forma de tabla
print(tabulate(tabla , headers=["t","v"], tablefmt="mixed_grid", floatfmt=".10f"))
plt.plot(ListaX,Listay)
plt.xlabel("Tiempo")
plt.ylabel("Velocidad")
plt.title('Funcion')
#Utilizamos plt para poder graficar
plt.grid()
plt.show()