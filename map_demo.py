from map import Labyrinth

test_lab = Labyrinth(10,10)
print test_lab.text_map()

print test_lab[(0,0)].make_description()
print test_lab[(1,1)].make_description()