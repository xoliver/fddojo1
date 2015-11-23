import sys

from .map import Labyrinth


class Game(object):
    MSG = ''
    INVALID_MSG = ''
    SIZE = (10, 10)

    def __init__(self):
        width, height = self.SIZE
        self.lab = Labyrinth(width, height)

    def start(self):
        self.show_message(self.MSG)

        while True:
            cmd = raw_input().lower()

            if not self.validate_command(cmd):
                self.show_message(self.INVALID_MSG)
                self.show_message(self.MSG)
            else:
                self.next_adventure(cmd)

    def validate_command(self):
        pass

    def show_message(self, message):
        sys.stdout.write(message)

    def next_adventure(self, cmd):
        msg = self.get_next_dest(cmd)
        self.show_message(msg)

    def get_next_dest(self, cmd):
        #TODO: talk to lab

        return 1


if __name__ == '__main__':
    game_book = object()

    game = Game(game_book)
    game.start()
