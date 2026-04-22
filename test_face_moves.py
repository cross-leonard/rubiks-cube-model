from cube import Cube


# cube = {
#     "U": ["W-1", "W", "W-2", 
#           "W", "W", "W", 
#           "W-4", "W", "W-3"],  # Up
#     "D": ["Y-1", "Y", "Y-2", 
#           "Y", "Y", "Y", 
#           "Y-4", "Y", "Y-3"],  # Down
#     "F": ["G", "G", "G", 
#           "G", "G", "G", 
#           "G", "G", "G"],  # Front
#     "B": ["B", "B", "B", 
#           "B", "B", "B", 
#           "B", "B", "B"],  # Back
#     "L": ["O", "O", "O", 
#           "O", "O", "O", 
#           "O", "O", "O"],  # Left
#     "R": ["R", "R", "R", 
#           "R", "R", "R", 
#           "R", "R", "R"],  # Right
# }

cube = Cube()

def cube_print(cube):
    print(cube.state["U"][0:3])
    print(cube.state["U"][3:6])
    print(cube.state["U"][6:])
    print()

    print(cube.state["F"][:3])
    print(cube.state["F"][3:6])
    print(cube.state["F"][6:])
    print()

    print(cube.state["R"][:3])
    print(cube.state["R"][3:6])
    print(cube.state["R"][6:])
    print()

    print(cube.state["B"][:3])
    print(cube.state["B"][3:6])
    print(cube.state["B"][6:])
    print()

    print(cube.state["L"][:3])
    print(cube.state["L"][3:6])
    print(cube.state["L"][6:])
    print()

    print(cube.state["D"][:3])
    print(cube.state["D"][3:6])
    print(cube.state["D"][6:])
    print()


cube_print(cube)





print('OUTCOME:')
print()

cube.D()

cube_print(cube)
