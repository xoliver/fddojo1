from map import Labyrinth

test_lab = Labyrinth(10,20)
print test_lab.text_map()

print test_lab[(0,0)].make_description()
print test_lab[(1,1)].make_description()

print test_lab.player_location
print test_lab.monster_location
room = test_lab.get_current_player_room()
print room.make_description()

test_lab.move_player("north")
print test_lab.player_location