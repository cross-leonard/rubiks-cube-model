
def cycle_clockwise(
    face1: str,
    slice1: slice,
    face2: str,
    slice2: slice,
    face3: str,
    slice3: slice,
    face4: str,
    slice4: slice,
) -> None:
    """Clockwise 4-way cycle for contiguous strips (rows)."""
    temp = cube[face1][slice1]
    cube[face1][slice1] = cube[face4][slice4]
    cube[face4][slice4] = cube[face3][slice3]
    cube[face3][slice3] = cube[face2][slice2]
    cube[face2][slice2] = temp


def cycle_indices_clockwise(
    face1: str,
    indices1: list[int],
    face2: str,
    indices2: list[int],
    face3: str,
    indices3: list[int],
    face4: str,
    indices4: list[int],
) -> None:
    """Clockwise 4-way cycle for strips that are not simple slices."""
    temp = [cube[face1][index] for index in indices1]

    for i in range(len(indices1)):
        target_index = indices1[i]
        source_index = indices4[i]
        cube[face1][target_index] = cube[face4][source_index]

    for i in range(len(indices4)):
        target_index = indices4[i]
        source_index = indices3[i]
        cube[face4][target_index] = cube[face3][source_index]
    
    for i in range(len(indices3)):
        target_index = indices3[i]
        source_index = indices2[i]
        cube[face3][target_index] = cube[face2][source_index]
    
    for i in range(len(indices2)):
        target_index = indices2[i]
        source_index = temp[i]
        cube[face2][target_index] = cube[face1][source_index]


def rotate_face_clockwise(face: str) -> None:
    old = cube[face][:]
    cube[face][0] = old[6]
    cube[face][1] = old[3]
    cube[face][2] = old[0]
    cube[face][3] = old[7]
    cube[face][4] = old[4]
    cube[face][5] = old[1]
    cube[face][6] = old[8]
    cube[face][7] = old[5]
    cube[face][8] = old[2]


