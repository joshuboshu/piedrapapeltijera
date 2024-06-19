'''
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
 *   o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
 */
'''

from os import system
from getpass_asterisk.getpass_asterisk import getpass_asterisk

def piedra_papel_tijera():
    seguir = ''  # Variable para controlar si se sigue jugando
    c = 1  # Contador de partidas
    w1 = 0  # Contador de partidas ganadas por el jugador 1
    w2 = 0  # Contador de partidas ganadas por el jugador 2
    jugadas = ['R', 'P', 'S']  # Lista de jugadas válidas
    jugador_1 = input('Jugador número 1, ingrese su nombre: ').lower().title()
    jugador_2 = input('Jugador número 2, ingrese su nombre: ').lower().title()
    system('clear')  # Limpia la pantalla al inicio del juego
    #system('cls') si tienes windows

    while seguir != 'N':
        print(f'Partida número: [{c}]')
        print('Estas son las opciones:\n[R]: [PIEDRA]\n[P]: [PAPEL]\n[S]: [TIJERA]')

        # Jugada del jugador 1
        player_1 = getpass_asterisk(f'{jugador_1}, haga su elección: ').upper()
        while player_1 not in jugadas:
            player_1 = getpass_asterisk(f'Ingrese una jugada válida, {jugador_1}: ').upper()

        # Jugada del jugador 2
        player_2 = getpass_asterisk(f'{jugador_2}, haga su elección: ').upper()
        while player_2 not in jugadas:
            player_2 = getpass_asterisk(f'Ingrese una jugada válida, {jugador_2}: ').upper()

        # Determina el ganador o si es empate
        if player_1 == player_2:
            print('¡Eso es un empate!')
        elif (player_1 == 'R' and player_2 == 'S') or (player_1 == 'S' and player_2 == 'P') or (
                player_1 == 'P' and player_2 == 'R'):
            w1 += 1
            print('*' * 50)
            print(
                f'Ha ganado {jugador_1}\nLa cuenta va así:\n{jugador_1}: {w1} partidas ganadas\n{jugador_2}: {w2} partidas ganadas')
            print('*' * 50)
        else:
            w2 += 1
            print('*' * 50)
            print(
                f'Ha ganado {jugador_2}\nLa cuenta va así:\n{jugador_1}: {w1} partidas ganadas\n{jugador_2}: {w2} partidas ganadas')
            print('*' * 50)

        c += 1
        seguir = input('¿Desean seguir jugando? [Y/N] ').upper()
        while seguir != 'Y' and seguir != 'N':
            seguir = input('Ingrese una opción válida: ').upper()

        system('clear')  # Limpia la pantalla al inicio del juego
        #system('cls') si tienes windows

    print('*' * 50)
    print(f'GRACIAS POR JUGAR {jugador_1.upper()} Y {jugador_2.upper()}')
    print('*' * 50)


# Llama a la función principal
piedra_papel_tijera()
