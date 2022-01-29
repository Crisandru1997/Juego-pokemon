from constantes import *

class Batalla:
    
    def __init__(self, pokemon_1, pokemon_2):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.turno_actual = 0
    
    def ejecuta_turno(self, turno):
        comando_1 = turno.comando_1
        comando_2 = turno.comando_2
        ataque_1 = None
        ataque_2 = None
        
        if ATACAR in comando_1.accion.keys():
            ataque_1 = self.pokemon_1.ataque[comando_1.accion[ATACAR]]
        if ATACAR in comando_2.accion.keys():
            ataque_2 = self.pokemon_2.ataque[comando_2.accion[ATACAR]]
        
        # Formula de ataque.
        self.pokemon_2.vida_actual -= ataque_1.poder
        self.pokemon_1.vida_actual -= ataque_2.poder
        
        self.turno_actual += 1
        
    def finalizo(self):
        finalizado = self.pokemon_1.vida_actual <= 0 or self.pokemon_2.vida_actual <= 0
        if finalizado:
            self.ganador()
        return finalizado

    def imprimir_estado(self):
        print(self.pokemon_1.nombre+" tiene "+str(self.pokemon_1.vida_actual)+" de vida!")
        print(self.pokemon_2.nombre+" tiene "+str(self.pokemon_2.vida_actual)+" de vida!")
    
    def ganador(self):
        if self.pokemon_1.vida_actual <= 0 < self.pokemon_2.vida_actual:
            print(self.pokemon_2.nombre+"  gano en "+str(self.turno_actual)+" turnos!")
        elif self.pokemon_2.vida_actual <= 0 < self.pokemon_1.vida_actual:
            print(self.pokemon_1 .nombre+"  gano en "+str(self.turno_actual)+" turnos!")
        else:
            print("Empatados!")
    
class Pokemon:
    
    def __init__(self, nombre, nivel, tipo_1, tipo_2):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo_1 = tipo_1
        self.tipo_2 = tipo_2
        self.ataque = [] # Vector de ataques 
        self.estadisticas = {}
        self.estado_actual = 0
        self.vida_actual = 0

class Ataque:
    
    def __init__(self, nombre, tipo, categoria, pp, poder, exactitud):
        self.nombre = nombre
        self.tipo = tipo
        self.categoria = categoria
        self.pp = pp
        self.poder = poder
        self.exactitud = exactitud
        
class Comando:
    def __init__(self, accion):
        self.accion = accion

class Turno:
    
    def __init__(self):
        self.comando_1 = None
        self.comando_2 = None
    
    # Definimos esta funcion para esperar que los dos pokemones
    # elijan su opción, es decir, el primer pokemon ejecuta su accion
    # y queda a la espera hasta que el pokemon 2 ejecute su acción igualmente.
    def puede_empezar(self):
        return self.comando_1 is not None and self.comando_2 is not None










