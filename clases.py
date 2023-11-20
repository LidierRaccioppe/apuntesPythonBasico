import math

class PrimerCuadranteError (Exception):
    def __int__(self, coordenada):
        self.coordenada = coordenada

    def __str__(self):
        return "Error de coordenadas:" + self.coordenada + " : No es un punto del primer cuadrante "
class Punto:
    """
    Clase que define a un punto en un plano bidimensional, que sea perteneciente al primer cuadrante

    :exception: PrimerCuadranteError
    """
    def __init__ (self, x = 0, y = 0):
        self.setX(x)
        self.setY(y)

    def getY(self):
        return self.__y

    def getX(self):
        return self.__x
    def getY (self):
        return self.__y
    def setX (self, x):
        if x >= 0:
            self.__x = x
        else:
            raise PrimerCuadranteError("X")

    def setY (self, y):
        if y >= 0:
            self.__y = y
        else:
            raise PrimerCuadranteError("Y")

    x = property(getX, setX)
    y = property(getY, setY)



try:
    print("trata de esclavos errores")
    raise (Exception("Este es otro error indeterminado"))
    p1 = Punto (1,3)

    p2 = Punto (1,-3)
except PrimerCuadranteError as error:
    print (error)
except Exception as error:
    print(error)
else:
    print("Solo se executa no hay errores")
finally:
    print("Se ejecuta cuando el finladi se dio por completo")







# p1 = Punto(1.0, 2.3)


# p1.x=15.66

# print ("Coordenadas del punto: "+str(p1.x) + ", "+str(p1.y))




# print(type (p1))




class Circulo (Punto):
    """
    Clase que representa un cirulo centrado en un punto
    """
    def __init__(self, x=0 , y=0, r=1):
        Punto.__init__(self, x, y)
        self.r=r

    def superficie (self):
        return math.pi * math.pow(self.r,2)

    def perimetro (self):
        return 2* math.pi * self.r
    def __gt__(self, otro):
        return self.superficie()>otro.superficie()
    def __lt__(self, otro):
        return self.superficie()<otro.superficie()
    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y and self.r == otro.r
    """__ne__
       __ge__
       __le__"""


# print(p1.x, p1.y)


## p1=Punto(1,3)
c1 = Circulo(1,5,3)
c2 = Circulo(1,3,8)
c3 = Circulo()

print (c1>c2)




print ("La superficie es : " + str(c1.superficie()))





class Cilindro (Circulo):
    def __init__(self, x = 0, y = 0, r=1, h=1):
        super().__init__(x,y,r)
        self.h = h

    def superficie(self):
        return super().superficie()*2 + super().perimetro()*self.h

    def __str__(self):
        return "Cilindro con un centro en " + str(self.x) +", "+str(self.y)+ " y radio = " + str(self.r) + " y altura = " + str(self.h)




cil = Cilindro (1,5,3,2)

print("superifice : "+ str(cil.superficie()))

print(cil)

cil.__str__()















