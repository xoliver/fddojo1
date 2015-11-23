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
            move = random.choice(MOVES)

            if self.failed_last_move and move == self.last_move:
                continue
            else:
                break

        self.history.append(move)
        self.last_move = move

    def result(self, success, room):
        self.failed_last_move = not success
        self.room = room
