
# Esta es una clase sencilla que se crea para facilitar
# la anexion de funcionalidades al codigo en un futuro
# se usa para identifiar al usuario  otros atributos que puuedan servir mas adelante
class User:
    def __init__(self, name= 'Default'):
        self.name = name
    
    
    def __str__(self):
        return 'name: ' + self.name