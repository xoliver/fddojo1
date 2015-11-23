import sys

from .map import Labyrinth
from constants import DIRECTIONS


class Game(object):
    MSG = 'This is a Labyrinth game'
    INVALID_MSG = 'Please give the direction.'
    SIZE = (10, 10, )
    VALID_DIRECTIONS = set(['west', 'east', 'north', 'south'])

    def __init__(self):
        width, height = self.SIZE
        self.lab = Labyrinth(width, height)

    def start(self):
        self.show_message(self.MSG)

        while True:
            cmd = raw_input().lower().split()

            direction = self.get_direction(cmd)

            if not direction:
                self.show_message(self.INVALID_MSG)
            else:
                self.next_adventure(direction)

    def get_direction(self, cmd):
        direction = self.VALID_DIRECTIONS.intersection(set(cmd))

        if direction and len(direction) == 1:
            return DIRECTIONS.get(direction[0])

        return False

    def show_message(self, message):
        sys.stdout.write(message)

    def next_adventure(self, direction):
        current_room = self.lab.move_player(direction)
        self.show_message(current_room.make_description())


if __name__ == '__main__':
    game_book = object()

    game = Game(game_book)
    game.start()
