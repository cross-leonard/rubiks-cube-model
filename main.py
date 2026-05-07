"""Entrypoint for computing edge memo from a scrambled cube."""

from cube import Cube
from solver import get_edge_memo


def main():
    # Create a fresh solved cube
    cube = Cube()

    # Enter your scramble here
    scramble = input("Enter scramble: ")

    # Apply the scramble to the cube
    cube.apply_scramble(scramble)

    print(cube)

if __name__ == "__main__":
    main()