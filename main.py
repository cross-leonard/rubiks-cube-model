"""Entrypoint for computing edge memo from a scrambled cube."""

from cube import Cube
from solver import get_edge_memo


def main() -> None:
    """Create a cube, optionally scramble it, and print the edge memo."""
    cube = Cube()
    
    # Prompt user for scramble
    print("Enter cube scramble (space-separated moves, e.g., 'R U R' U'):")
    print("Press Enter to get memo for solved cube.")
    scramble = input().strip()
    
    if scramble:
        try:
            cube.apply_scramble(scramble)
        except ValueError as e:
            print(f"Error: {e}")
            return
    
    # Get and print the edge memo
    memo = get_edge_memo(cube)
    print(f"Edge memo: {memo}")


if __name__ == "__main__":
    main()
