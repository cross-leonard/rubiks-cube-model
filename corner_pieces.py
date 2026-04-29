"""Static corner-piece mappings used by future corner tracing helpers."""

# Letter to sticker position mapping (Speffz corners).
CORNER_POSITIONS = {
    # U face
    "A": ("U", 0),  # UBL
    "B": ("U", 2),  # UBR
    "C": ("U", 8),  # UFR
    "D": ("U", 6),  # UFL

    # L face
    "E": ("L", 0),  # LUB
    "F": ("L", 2),  # LUF
    "G": ("L", 8),  # LDF
    "H": ("L", 6),  # LDB

    # F face
    "I": ("F", 0),  # FUL
    "J": ("F", 2),  # FUR
    "K": ("F", 8),  # FDR
    "L": ("F", 6),  # FDL

    # R face
    "M": ("R", 0),  # RUF
    "N": ("R", 2),  # RUB
    "O": ("R", 8),  # RDB
    "P": ("R", 6),  # RDF

    # B face
    "Q": ("B", 0),  # BUR
    "R": ("B", 2),  # BUL
    "S": ("B", 8),  # BDL
    "T": ("B", 6),  # BDR

    # D face
    "U": ("D", 0),  # DFL
    "V": ("D", 2),  # DFR
    "W": ("D", 8),  # DBR
    "X": ("D", 6),  # DBL
}

# Sticker-oriented corner piece definitions (24 entries, one per sticker orientation).
CORNER_PIECES = {
    "UBL": (("U", 0), ("B", 2), ("L", 0)),
    "UBR": (("U", 2), ("R", 2), ("B", 0)),
    "UFR": (("U", 8), ("F", 2), ("R", 0)),
    "UFL": (("U", 6), ("L", 2), ("F", 0)),

    "LUB": (("L", 0), ("U", 0), ("B", 2)),
    "LUF": (("L", 2), ("F", 0), ("U", 6)),
    "LDF": (("L", 8), ("D", 0), ("F", 6)),
    "LDB": (("L", 6), ("B", 8), ("D", 6)),

    "FUL": (("F", 0), ("U", 6), ("L", 2)),
    "FUR": (("F", 2), ("R", 0), ("U", 8)),
    "FDR": (("F", 8), ("D", 2), ("R", 6)),
    "FDL": (("F", 6), ("L", 8), ("D", 0)),

    "RUF": (("R", 0), ("U", 8), ("F", 2)),
    "RUB": (("R", 2), ("B", 0), ("U", 2)),
    "RDB": (("R", 8), ("D", 8), ("B", 6)),
    "RDF": (("R", 6), ("F", 8), ("D", 2)),

    "BUR": (("B", 0), ("U", 2), ("R", 2)),
    "BUL": (("B", 2), ("L", 0), ("U", 0)),
    "BDL": (("B", 8), ("D", 6), ("L", 6)),
    "BDR": (("B", 6), ("R", 8), ("D", 8)),

    "DFL": (("D", 0), ("F", 6), ("L", 8)),
    "DFR": (("D", 2), ("R", 6), ("F", 8)),
    "DBR": (("D", 8), ("B", 6), ("R", 8)),
    "DBL": (("D", 6), ("L", 6), ("B", 8)),
}

CORNER_LETTER = {
    "UBL": "A",
    "UBR": "B",
    "UFR": "C",
    "UFL": "D",

    "LUB": "E",
    "LUF": "F",
    "LDF": "G",
    "LDB": "H",

    "FUL": "I",
    "FUR": "J",
    "FDR": "K",
    "FDL": "L",

    "RUF": "M",
    "RUB": "N",
    "RDB": "O",
    "RDF": "P",

    "BUR": "Q",
    "BUL": "R",
    "BDL": "S",
    "BDR": "T",

    "DFL": "U",
    "DFR": "V",
    "DBR": "W",
    "DBL": "X",
}

HOME_COLORS = {
    "U": "W",
    "D": "Y",
    "F": "F",
    "B": "B",
    "L": "O",
    "R": "R",
}

# For each corner sticker, list the other two stickers on the same piece.
CORNER_ADJACENT = {
    ("U", 0): (("B", 2), ("L", 0)),
    ("U", 2): (("R", 2), ("B", 0)),
    ("U", 8): (("F", 2), ("R", 0)),
    ("U", 6): (("L", 2), ("F", 0)),

    ("L", 0): (("U", 0), ("B", 2)),
    ("L", 2): (("F", 0), ("U", 6)),
    ("L", 8): (("D", 0), ("F", 6)),
    ("L", 6): (("B", 8), ("D", 6)),

    ("F", 0): (("U", 6), ("L", 2)),
    ("F", 2): (("R", 0), ("U", 8)),
    ("F", 8): (("D", 2), ("R", 6)),
    ("F", 6): (("L", 8), ("D", 0)),

    ("R", 0): (("U", 8), ("F", 2)),
    ("R", 2): (("B", 0), ("U", 2)),
    ("R", 8): (("D", 8), ("B", 6)),
    ("R", 6): (("F", 8), ("D", 2)),

    ("B", 0): (("U", 2), ("R", 2)),
    ("B", 2): (("L", 0), ("U", 0)),
    ("B", 8): (("D", 6), ("L", 6)),
    ("B", 6): (("R", 8), ("D", 8)),

    ("D", 0): (("F", 6), ("L", 8)),
    ("D", 2): (("R", 6), ("F", 8)),
    ("D", 8): (("B", 6), ("R", 8)),
    ("D", 6): (("L", 6), ("B", 8)),
}
