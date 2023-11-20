def saludar (lengua = "en"):
    def saludar_es():
        print("Hola")
    def saludar_gl():
        print("Ola")
    def saludar_it():
        print("Ciao")
    def saludar_en():
        print("Hello")

    # Un diccionario para despues poder retornar una función
    # Se debe de manter los tipos iguales
    saludo_idiomas = {
        "es": saludar_es,
        "gl": saludar_gl,
        "it": saludar_it,
        "en": saludar_en
    }
    return saludo_idiomas[lengua]

f = saludar("es") # se guarda en la variable la función
print(f)
f()