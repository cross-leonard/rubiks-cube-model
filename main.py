"""Small entrypoint for printing the cube state."""

from cube import Cube

def main() -> None:
    """Create a solved cube and print its state."""
    cube = Cube()
    print(cube.state)


if __name__ == "__main__":
    main()
