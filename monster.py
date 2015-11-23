import random

MOVES = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E',
}


class Monster(object):

    def __init__(self):
        self.room = None
        self.failed_last_move = False
        self.history = []
        self.last_move = None

    def action(self):
        while True:
            move = random.choice(MOVES.keys())

            if self.failed_last_move and move == self.last_move:
                continue
            else:
                break

        self.history.append(move)
        self.last_move = move

    def result(self, new_room):
        if new_room == self.room:
            self.failed_last_move = True
        else:
            self.room = new_room
