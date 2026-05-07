"""Helpers for identifying edge pieces from the current cube state."""

from edge_pieces import EDGE_ADJACENT, EDGE_PIECES, HOME_COLORS as EDGE_HOME_COLORS, EDGE_LETTER


def get_edge_at_position(cube, face, index):
    """
    Look at a sticker on the cube and figure out which edge piece it belongs to.
    
    For example, if we look at position (U, 7) we see a color there.
    We also check the adjacent sticker (the other half of the same edge piece).
    Then we compare those two colors to every known edge piece until we find a match.
    
    Returns:
        piece_name  - e.g. "UF" meaning the Up-Front edge piece
        orientation - 0 means the piece is not flipped, 1 means it is flipped
    """

    # Step 1: Read the color of the sticker we are looking at
    color1 = cube.state[face][index]

    # Step 2: Find the other sticker on the same edge piece
    # EDGE_ADJACENT tells us: "if you are looking at (face, index),
    # the other half of that edge is at (face2, index2)"
    face2, index2 = EDGE_ADJACENT[(face, index)]
    color2 = cube.state[face2][index2]

    # Step 3: Loop through every known edge piece and check if the colors match
    for piece_name, sticker_positions in EDGE_PIECES.items():

        # Each edge piece has two home sticker positions
        # e.g. the "UF" piece lives at ("U", 7) and ("F", 1) when solved
        home_sticker_1 = sticker_positions[0]   # e.g. ("U", 7)
        home_sticker_2 = sticker_positions[1]   # e.g. ("F", 1)

        # Get the face letter for each home sticker position
        home_face_1 = home_sticker_1[0]   # e.g. "U"
        home_face_2 = home_sticker_2[0]   # e.g. "F"

        # Look up what color belongs on each face when the cube is solved
        # e.g. "U" -> "W" (white), "F" -> "F" (green), etc.
        home_color_1 = EDGE_HOME_COLORS[home_face_1]
        home_color_2 = EDGE_HOME_COLORS[home_face_2]

        # Check if the colors match in the normal (unflipped) orientation
        # i.e. color1 matches the first home color, color2 matches the second
        not_flipped = (color1 == home_color_1 and color2 == home_color_2)
        if not_flipped:
            return piece_name, 0

        # Check if the colors match in the flipped orientation
        # i.e. the two stickers are swapped compared to normal
        flipped = (color1 == home_color_2 and color2 == home_color_1)
        if flipped:
            return piece_name, 1

    # If we get here, no edge piece matched - the cube state must be invalid
    raise ValueError("Invalid cube state: could not find a matching edge piece")


def is_edge_solved(cube, piece_name):
    """
    Check if a specific edge piece is sitting in its correct home position,
    with the correct orientation (not flipped).
    
    Returns True if the piece is solved, False otherwise.
    """
    # Find where this piece lives when the cube is solved
    home_face, home_index = EDGE_PIECES[piece_name][0]

    # Look at what piece is actually sitting there right now
    piece_found, orientation = get_edge_at_position(cube, home_face, home_index)

    # It's only truly solved if the right piece is there AND it's not flipped
    return piece_found == piece_name and orientation == 0


def get_edge_memo(cube):
    """
    Generate the Speffz letter memo string for all unsolved edges.
    
    This follows the 3-style / M2 blind solving method:
    - We have a buffer piece (UR). We don't letter that one.
    - We find unsolved pieces and trace cycles through them.
    - Each piece gets a Speffz letter added to the memo string.
    
    How cycles work:
    - Pick the first unsolved piece. Write its letter. That starts a new cycle.
    - Then look at what piece is currently sitting in the UR buffer's old spot
      ... actually, we follow where the cycle leads:
      look at what piece is at the current target's home, write that letter, repeat.
    - When the cycle loops back to UR (or an already-solved piece), the cycle ends.
    - Then start a new cycle with the next unsolved piece.
    """

    memo = ""

    # Keep track of which pieces we have already handled
    # We start with "UR" because that is the buffer - we never letter it
    already_handled = {"UR"}

    # Keep looping until all edge pieces are accounted for
    while True:

        # --- Find the next unsolved piece to start a new cycle ---
        next_unsolved = None
        for piece_name in EDGE_PIECES:

            # Skip pieces we have already handled
            if piece_name in already_handled:
                continue

            # Check if this piece is already sitting in its correct home spot
            if not is_edge_solved(cube, piece_name):
                next_unsolved = piece_name
                break   # Found one - stop looking

        # If every piece is solved, we are done
        if next_unsolved is None:
            break

        # --- Start a new cycle from this unsolved piece ---
        # Write the letter for this piece to begin the cycle
        memo += EDGE_LETTER[next_unsolved]
        already_handled.add(next_unsolved)

        # Now follow the cycle:
        # Look at what piece is currently at next_unsolved's home position,
        # write its letter, then move to that piece's home, and repeat.
        current_face, current_index = EDGE_PIECES[next_unsolved][0]

        while True:
            # What piece is currently sitting at the position we are looking at?
            piece_found, orientation = get_edge_at_position(cube, current_face, current_index)

            # If we've looped back to the buffer (UR) or an already-handled piece,
            # this cycle is complete
            if piece_found == "UR" or piece_found in already_handled:
                break

            # Otherwise, write the letter for this piece and continue the cycle
            memo += EDGE_LETTER[piece_found]
            already_handled.add(piece_found)

            # Move to the home position of the piece we just found
            current_face, current_index = EDGE_PIECES[piece_found][0]

    return memo