"""Helpers for identifying edge and corner pieces from the current cube state."""

from edge_pieces import EDGE_ADJACENT, EDGE_PIECES, HOME_COLORS as EDGE_HOME_COLORS, EDGE_LETTER
from corner_pieces import (
    CORNER_ADJACENT,
    CORNER_PIECES,
    HOME_COLORS as CORNER_HOME_COLORS,
    CORNER_LETTER,
)

def get_edge_at_position(cube, face: str, index: int) -> tuple[str, int]:
    """Return the edge piece name and orientation at a sticker location."""

    color1 = cube.state[face][index]

    face2, index2 = EDGE_ADJACENT[(face, index)]
    color2 = cube.state[face2][index2]

    for piece_name, value in EDGE_PIECES.items():
        sticker1 = value[0]   # e.g. ("U", 7)
        sticker2 = value[1]   # e.g. ("F", 1)

        f1 = sticker1[0]      # "U"
        f2 = sticker2[0]      # "F"

        home_color1 = EDGE_HOME_COLORS[f1]
        home_color2 = EDGE_HOME_COLORS[f2]

        if color1 == home_color1 and color2 == home_color2:
            return piece_name, 0

        if color1 == home_color2 and color2 == home_color1:
            return piece_name, 1

    raise ValueError("Invalid cube state: edge not found")


def get_edge_memo(cube) -> str:
    """Generates a memo string for edge piece sequences"""
    memo = ""
    current_face = "U"
    current_index = 5
    piece_name, orientation = get_edge_at_position(cube, current_face, current_index)

    while piece_name != "UR":
        piece_name, orientation = get_edge_at_position(cube, current_face, current_index)
        memo += EDGE_LETTER[piece_name]
        current_face = piece_name[0]
        current_index = EDGE_PIECES[piece_name][0][1]

    return memo


def get_corner_at_position(cube, face: str, index: int) -> tuple[str, int]:
    """Return the corner piece name and orientation at a sticker location."""

    color1 = cube.state[face][index]

    (face2, index2), (face3, index3) = CORNER_ADJACENT[(face, index)]
    color2 = cube.state[face2][index2]
    color3 = cube.state[face3][index3]

    for piece_name, value in CORNER_PIECES.items():
        sticker1 = value[0]
        sticker2 = value[1]
        sticker3 = value[2]

        f1 = sticker1[0]
        f2 = sticker2[0]
        f3 = sticker3[0]

        home_color1 = CORNER_HOME_COLORS[f1]
        home_color2 = CORNER_HOME_COLORS[f2]
        home_color3 = CORNER_HOME_COLORS[f3]

        if color1 == home_color1 and color2 == home_color2 and color3 == home_color3:
            return piece_name, 0

        if color1 == home_color2 and color2 == home_color3 and color3 == home_color1:
            return piece_name, 1

        if color1 == home_color3 and color2 == home_color1 and color3 == home_color2:
            return piece_name, 2

    raise ValueError("Invalid cube state: corner not found")


def get_corner_memo(cube) -> str:
    """Generate a memo string for corner piece sequences."""

    memo = ""
    current_face = "U"
    current_index = 8
    piece_name, orientation = get_corner_at_position(cube, current_face, current_index)

    while piece_name != "UFR":
        piece_name, orientation = get_corner_at_position(cube, current_face, current_index)
        memo += CORNER_LETTER[piece_name]
        current_face = piece_name[0]
        current_index = CORNER_PIECES[piece_name][0][1]

    return memo