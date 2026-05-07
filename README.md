# Rubik's Cube Model

This Python project provides a data representation of a 3x3 Rubik's Cube and a simple CLI to apply scrambles.

Only two modules are required: `cube.py` (the cube model) and `main.py` (a tiny entrypoint to apply a scramble and print the cube).

**Features**
- In-memory 3x3 cube state with face-turn methods
- `apply_scramble()` accepts space-separated moves (e.g. "R U R' U'")
- Minimal CLI: run `python main.py` and enter a scramble

## Quickstart

Run the CLI and enter a scramble when prompted:

```bash
python main.py
# Enter scramble: R U R' U'
```

Programmatic example:

```python
from cube import Cube

c = Cube()
c.apply_scramble("R U R' U'")
print(c)
```

