# Maze (Esse algoritmo funciona para as maiorias das situações

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def walk_maze():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
#
#
# while not at_goal():
#     walk_maze()

# Algoritmo que resolver os bugs de situações em que o robô entrava em loop infinito.
# Obs.: Algumas funções não funcionam aqui dentro, pois pertece ao site https://reeborg.ca/
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()


def walk_maze():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


while not at_goal():
    walk_maze()
