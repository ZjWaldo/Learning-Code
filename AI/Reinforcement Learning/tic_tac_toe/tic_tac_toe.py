from helper_methods import *
from tic_tac_toe_learn import *
init_state = '000000000'
CIRCLE = 1
CROSS = 2

def print_row(r):
    for i in range(len(r)):
        if i == 0 or i == 1:
            print(r[i] + '|', end='')
        else:
            print(r[i], end='')
    print()

def print_line():
    for i in range(5):
        print('-', end='')
    print()

# Turns a state string into a tic tac toe grid
def print_state(state):
    print_row(state[0:3])
    print_line()
    print_row(state[3:6])
    print_line()
    print_row(state[6:9])

# Takes the current state, the index the current player chooses to mark, and outputs the new state
def human_update_state(old_state, id, player):
    new_state = ''
    for i in range(len(old_state)):
        if i == (id - 1):
            new_state = new_state + str(player)
        else:
            new_state = new_state + old_state[i]
    return new_state

def switch_player(player):
    if player == CIRCLE:
        return CROSS
    elif player == CROSS:
        return CIRCLE
    else:
        return -1

def print_victory(state, player):
    if rowComplete(state) or colComplete(state) or diaComplete(state):
        if player == CIRCLE:
            print('Circle won!')
        else:
            print('Cross won!')
    else:
        print('Tied!')


def h_vs_ai():
    return 5

def h_vs_h():
    player = CROSS
    index = 0
    cur_state = init_state
    print_state(cur_state)
    while not isComplete(cur_state):
        player = switch_player(player)
        if player == CIRCLE:
            index = int(input('Circle\'s turn. Please enter 1-9 to choose a square\n'))
        else:
            index = int(input('Cross\'s turn. Please enter 1-9 to choose a square\n'))

        while cur_state[index-1] != '0':
            index = int(input('That spot is already taken. Choose another.\n'))
        cur_state = human_update_state(cur_state, index, player)
        print_state(cur_state)
    print_victory(cur_state, player)

def init_game():
    while True:
        game_type = input("Press 0 to exit the game, 1 for human vs human, or 2 for human vs AI\n")

        if game_type == '0':
            exit()
        elif game_type == '1':
            h_vs_h()
        elif game_type == '2':
            print('2')
        else:
            print("Your selection did not make sense.")

init_game()