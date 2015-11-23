from constants import MOVES
from map import Labyrinth


if __name__ == '__main__':
    lab = Labyrinth(10, 10)

    while True:
        line = raw_input().lower()
        try:
            cmd, direction = line.split(' ')
        except:
            print 'NO IDEA WHAT YOU SAID'
            continue

        if cmd != 'go' and direction not in MOVES:
            print 'CANNOT UNDERSTAND COMMAND OR DIRECTION'

        room = lab.move_player(direction)
