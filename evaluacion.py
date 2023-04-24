###1promedio de un conjunto de numeros 

class PromedioNumeros () :
    def promedio_numeros (self, conjunto): 
         cantidad =len(conjunto)
         suma = sum (conjunto)
         promedio= suma/cantidad
         return promedio

    def imprimir_promedio(self, promedio):
         print("el promedio es:", promedio)

###2determinar si un numero es par o impar 
class Numero():
    def es_par (self, numero):
        if numero % 2==0:
            return True 
        else:
            return False


###3 calcular el factorial de un número 

class Factorial ():
    def calcular_factorial(self, numero):
        resultado =1
        for i in range (1, numero+1):
            resultado *=i 
        return resultado


###4determinar cuales son los números pares de una lista de números. 
#debe devolver una lista 

class Numeros ():
    def __init__ (self, lista):
        self.lista= lista
    
    def obtener_pares (self):
        pares = []
        for num in self.lista:
            if num % 2==0:
                pares.append(num)
        return pares




###5realizar la suma de los pares ordenados 

class SumaParesOrdenados ():
    def __init__(self, a, b):
        self.a = a
        self.b= b 

    
    def sumar (self, otro_par):
        return (self.a + otro_par.a , self.b + otro_par.b)