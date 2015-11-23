import random

from constants import MOVES


class Monster(object):

    def __init__(self):
        self.room = None
        self.last_move_failed = False
        self.history = []
        self.last_move = None

    def get_move(self):
        while True:
            move = random.choice(MOVES.keys())

            if self.last_move_failed and move == self.last_move:
                continue
            else:
                break

        self.history.append(move)
        self.last_move = move

    def move(self, new_room):
        if new_room == self.room:
            self.last_move_failed = True
        else:
            self.room = new_room
