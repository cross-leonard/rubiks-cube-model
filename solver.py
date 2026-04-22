from pieces import EDGE_ADJACENT, HOME_COLORS, EDGE_PIECES, EDGE_POSITIONS

def get_edge_at_position(self, face: str, index: int):
    """
    Returns (piece_name, orientation)
    orientation = 0 (correct) or 1 (flipped)
    """

    # Read the first sticker
    color1 = self.state[face][index]

    # Find the partner sticker
    face2, index2 = EDGE_ADJACENT[(face, index)]
    color2 = self.state[face2][index2]

    # Try to match these two colors to a home edge piece
    for piece_name, ((f1, i1), (f2, i2)) in EDGE_PIECES.items():
        home_color1 = HOME_COLORS[f1]
        home_color2 = HOME_COLORS[f2]

        # Correct orientation
        if color1 == home_color1 and color2 == home_color2:
            return piece_name, 0

        # Flipped orientation
        if color1 == home_color2 and color2 == home_color1:
            return piece_name, 1

    raise ValueError("Invalid cube state: edge not found")
