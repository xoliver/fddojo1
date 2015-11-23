import sys

from map import Labyrinth
from constants import DIRECTIONS, MOVES


class Game(object):
    MSG = 'This is a Labyrinth game\n'
    INVALID_MSG = 'Please give the direction.'
    SIZE = (10, 10, )
    VALID_DIRECTIONS = set(['west', 'east', 'north', 'south'])

    def __init__(self):
        width, height = self.SIZE
        self.lab = Labyrinth(width, height)

    def start(self):
        self.show_message(self.MSG)

        while True:
            line = raw_input().lower()
            try:
                cmd, direction = line.split(' ')
            except:
                print 'NO IDEA WHAT YOU SAID'
                continue

            if cmd != 'go' and direction not in MOVES:
                print 'CANNOT UNDERSTAND COMMAND OR DIRECTION'

            self.next_adventure(direction)
    #
    # def get_direction(self, line):
    #     direction = self.VALID_DIRECTIONS.intersection(set(cmd))
    #
    #     if direction and len(direction) == 1:
    #         return DIRECTIONS.get(direction.pop())
    #
    #     return False

    def show_message(self, message):
        sys.stdout.write(message)

    def next_adventure(self, direction):
        current_room = self.lab.move_player(direction)
        self.show_message(current_room.make_description())


if __name__ == '__main__':
    game_book = object()

    game = Game()
    game.start()
