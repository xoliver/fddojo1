DIRECTIONS = {
    "north": (0, 1),
    "west": (-1, 0),
    "south": (0, -1),
    "east": (1, 0)
}


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

    def __getitem__(self,key):
        x, y = key
        return self.layout[x][y]

    def __init__(self, width, height):
        self.width = width
        self.height = height

        layout = []
        for _ in range(self.height):
            # To start out, just do a "maze" with doors between all rooms.
            row = []
            for _ in range(self.width):
                room = Room()
                room.doors = ["north", "south", "east", "west"]
                row.append(room)
            layout.append(row)

        # Remove the doors in the outer walls
        for room in layout[0]:
            room.doors.remove("north")
        for inner_row in layout:
            inner_row[0].doors.remove("west")
            inner_row[-1].doors.remove("east")
        for room in layout[-1]:
            room.doors.remove("south")

        layout[2][2].doors.remove("south")
        self.layout = layout

    def text_map(self):
        """
        Return maze table in ASCII
        For debugging purposes
        "Borrowed" from http://code.activestate.com/recipes/252127-maze-generator/
        """

        result = '.' + self.width*'_.'
        result += '\n'

        for i in range(self.height):
          result += '|'

          for j in range(self.width):
            if i==self.height-1 or "south" not in self.layout[i][j].doors:
              result += '_'
            else:
              result += ' '
            if j==self.width-1 or "east" not in self.layout[i][j].doors:
              result += '|'
            else:
              result += '.'

          result += '\n'

        return result
