from math import sqrt

from constants import (
    NORTH, SOUTH, EAST, WEST, DIRECTIONS,
    SOUND_THRESHOLD,
)
from random import randint


class Room(object):
    doors = []

    def make_description(self):
        description = "You are in a room.\n"
        for direction in self.doors:
            description += "There is a door to the {}\n".format(direction)

        return description


class Labyrinth(object):
    player_location = None
    monster_location = None
    layout = None
    width = None
    height = None

    def __getitem__(self, key):
        x, y = key
        return self.layout[x][y]

    def __init__(self, width, height):
        self.width = width
        self.height = height

        layout = []
        for _ in range(self.width):
            # To start out, just do a "maze" with doors between all rooms.
            row = []
            for _ in range(self.height):
                room = Room()
                room.doors = [NORTH, SOUTH, EAST, WEST]
                row.append(room)
            layout.append(row)

        # Remove the doors in the outer walls
        for room in layout[0]:
            room.doors.remove(WEST)
        for inner_column in layout:
            inner_column[0].doors.remove(SOUTH)
            inner_column[-1].doors.remove(NORTH)
        for room in layout[-1]:
            room.doors.remove(EAST)

        self.layout = layout

        self.player_location = self.get_random_location()
        self.monster_location = self.get_random_location()

    def get_random_location(self):
        return randint(0, self.width-1), randint(0, self.height-1)

    def player_hears(self):
        return self._calculate_sound(
            self.monster_location, self.player_location
        )

    def monster_hears(self):
        return self._calculate_sound(
            self.player_location, self.monster_location
        )

    def _calculate_sound(self, other, listener):
        distance = sqrt(
            (other[0] - listener[0]) ** 2 + (other[1] - listener[1] ** 2)
        )

        if distance > SOUND_THRESHOLD:
            return distance

    def text_map(self):
        """
        Return maze table in ASCII
        For debugging purposes
        "Borrowed" from http://code.activestate.com/recipes/252127-maze-generator/
        """

        result = '.' + self.width*'_.'
        result += '\n'

        for j in range(self.height-1, -1, -1):
          result += '|'

          for i in range(self.width):
            if SOUTH not in self.layout[i][j].doors:
              result += '_'
            else:
              result += ' '
            if EAST not in self.layout[i][j].doors:
              result += '|'
            else:
              result += '.'

          result += '\n'

        return result

    def get_current_player_room(self):
        x, y = self.player_location
        return self.layout[x][y]

    def move_player(self, direction):
        current_room = self.get_current_player_room()
        print current_room.make_description()
        if direction not in current_room.doors:
            print "You cannot move in this direction"
            return current_room
        else:
            current_x, current_y = self.player_location
            change_x, change_y = DIRECTIONS[direction]
            self.player_location = current_x + change_x, current_y + change_y
            print "You moved {}.".format(direction)
            return self.get_current_player_room()
