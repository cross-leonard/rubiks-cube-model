

EDGE_POSITIONS = {

    # U face
    "A": ("U", 1),  # UB
    "B": ("U", 5),  # UR
    "C": ("U", 7),  # UF
    "D": ("U", 3),  # UL

    # L face
    "E": ("L", 1),  # LU
    "F": ("L", 5),  # LF
    "G": ("L", 7),  # LD
    "H": ("L", 3),  # LB

    # F face
    "I": ("F", 1),  # FU
    "J": ("F", 5),  # FR
    "K": ("F", 7),  # FD
    "L": ("F", 3),  # FL

    # R face
    "M": ("R", 1),  # RU
    "N": ("R", 5),  # RB
    "O": ("R", 7),  # RD
    "P": ("R", 3),  # RL

    # B face
    "Q": ("B", 1),  # BU
    "R": ("B", 5),  # BL
    "S": ("B", 7),  # BD
    "T": ("B", 3),  # BR

    # D face
    "U": ("D", 1),  # DF
    "V": ("D", 5),  # DR
    "W": ("D", 7),  # DB
    "X": ("D", 3),  # DL
}


print(EDGE_POSITIONS["A"], EDGE_POSITIONS["M"])