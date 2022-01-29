from constantes import *
from models import *

# Definimos los pokemon con sus estados.
pokemon_1 = Pokemon("Bulbasaur", 100, "césped", "veneno")
pokemon_2 = Pokemon("Charmander", 100, "fuego", None)

# Vida actual del pokemon.
pokemon_1.vida_actual = 45
pokemon_2.vida_actual = 39

# Estadisticas de los pokemon.
pokemon_1.estadisticas = {
    HP: 45,
    ATTACK: 49,
    DEFENSE: 49,
    SPATTACK: 65,
    SPDEFENSE: 65,
    SPEED: 45,
}

pokemon_2.estadisticas = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTACK: 80,
    SPDEFENSE: 65,
    SPEED: 65,
}

# Definimos los ataques
pokemon_1.ataque = [
    Ataque("rasguño", "normal", FISICO, 10, 10, 100),
]
pokemon_2.ataque = [
    Ataque("rasguño", "normal", FISICO, 10, 10, 100),
]

# Iniciamos la batalla
batalla = Batalla(pokemon_1, pokemon_2)

def pedir_comando(pokemon):
    comando = None
    while not comando: # Mientras no tenga el comando definido.
        comando_tmp = input("Que debería hacer el "+pokemon.nombre+"?").split(" ")
        if len(comando_tmp) == 2:
            try:
                if comando_tmp[0] == ATACAR and 0 <= int(comando_tmp[1]) < 4:
                    comando = Comando({ATACAR: int(comando_tmp[1])})
                    print(comando_tmp)
            except Exception:
                pass
    return comando

while not batalla.finalizo(): # Mientras la batalla no finalice (mientras no pierda algun pokemon)
    # Pedir a los entrenadores el comando que realizara el pokemon
    comando_1 = pedir_comando(pokemon_1)
    comando_2 = pedir_comando(pokemon_2)
    
    turno = Turno()
    turno.comando_1 = comando_1
    turno.comando_2 = comando_2
    
    if turno.puede_empezar():
        # Ejecutamos el turno
        batalla.ejecuta_turno(turno)
        batalla.imprimir_estado()
