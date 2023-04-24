#test ejercicio1

from evaluacion import PromedioNumeros  

#instancio la clase 
mi_promedio = PromedioNumeros()

#creo un conjunto de números 
numeros = {10, 20, 30, 40, 50}

promedio = mi_promedio.promedio_numeros(numeros)

mi_promedio.imprimir_promedio(promedio)



#test ejercicio2
from evaluacion import Numero

num = Numero()
if num.es_par(7):
    print("7 es par")
else:
    print("7 es impar")
 
num= Numero()
if num.es_par(100):
    print("100 es par")
else:
    print("100 es impar")

####test ejercicio3 

from evaluacion import Factorial

fact =Factorial()
num = 5
mi_factorial = fact.calcular_factorial(num)
print("el factorial del numero",num,"es",mi_factorial)

###test ejercicio 4

from evaluacion import Numeros

numeros= Numeros([1, 2, 3, 4, 5,16,18, 98,101])

pares = numeros.obtener_pares()
print(pares)

###test ejercicio 5 

from evaluacion import SumaParesOrdenados
# Creamos dos objetos de la clase SumaParesOrdenados
par1 = SumaParesOrdenados(11, 2)
par2 = SumaParesOrdenados(28, 3)

# Llamamos al método sumar del primer objeto pasando el segundo objeto como argumento
resultado = par1.sumar(par2)

# Imprimimos el resultado
print(resultado)
