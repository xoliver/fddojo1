NORTH = "north"
SOUTH = "south"
EAST = "east"
WEST = "west"

MOVES = (NORTH, SOUTH, EAST, WEST)


DIRECTIONS = {
    NORTH: (0, 1),
    WEST: (-1, 0),
    SOUTH: (0, -1),
    EAST: (1, 0)
}


OPPOSITE_MOVES = {
    NORTH: SOUTH,
    SOUTH: NORTH,
    WEST: EAST,
    EAST: WEST,
}

SOUND_THRESHOLD = 4
