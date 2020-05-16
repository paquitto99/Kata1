from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'

def quienGana(player, ai):
    if player == ai:
        winner = "Empate!"
        control = 1
    elif player > ai:
        winner = "Ganaste!"
        control = 2
    else:
        winner = "Perdiste!"
        control = 3
    
    if ai == 0 and player == 2:
        winner = "Perdiste!"
        control = 4
     
    return winner

# Entry Point
def Game():
    ai = randint(0,2)
    
        
    playerName = input("Introduce tu nombre PLAYER ONE.:")
    player = int(input("Elige 1.- PIEDRA, 2.- PAPEL o 3.- TIJERAS.:"))
    print("Perfecto " + playerName +  " has elegido " + str(options[player-1]) + ", ahora veremos si le ganas a nuestra IA...")
    x = input("Pulsa una INTRO para jugartela . . . ")
    print ("La IA ha elegido " + options[ai] + " así pues... ")
    winner = quienGana(player-1, ai)
    print(winner)

#  invoco el juego
a =  Game()
 