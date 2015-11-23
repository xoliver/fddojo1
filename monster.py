import random

from constants import MOVES


class Monster(object):

    def __init__(self):
        self.room = None
        self.last_move_failed = False
        self.history = []
        self.last_move = None
        self.could_hear_player = False

    def get_move(self):
        if self.could_hear_player and not self.last_move_failed:
            move = self.last_move
        else:
            while True:
                move = random.choice(MOVES)

                if self.last_move_failed and move == self.last_move:
                    continue
                else:
                    break

        self.history.append(move)
        self.last_move = move
        return move

    def move(self, new_room, can_hear_player):
        self.could_hear_player = can_hear_player

        if new_room == self.room:
            self.last_move_failed = True
            return

        self.room = new_room
