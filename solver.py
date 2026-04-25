"""Helpers for identifying edge pieces from the current cube state."""

from pieces import EDGE_ADJACENT, EDGE_PIECES, HOME_COLORS

def get_edge_at_position(cube, face: str, index: int) -> tuple[str, int]:
    """Return the edge piece name and orientation at a sticker location."""

    color1 = cube.state[face][index]

    face2, index2 = EDGE_ADJACENT[(face, index)]
    color2 = cube.state[face2][index2]

    for piece_name, ((f1, _), (f2, _)) in EDGE_PIECES.items():
        home_color1 = HOME_COLORS[f1]
        home_color2 = HOME_COLORS[f2]

        if color1 == home_color1 and color2 == home_color2:
            return piece_name, 0

        if color1 == home_color2 and color2 == home_color1:
            return piece_name, 1

    raise ValueError("Invalid cube state: edge not found")
