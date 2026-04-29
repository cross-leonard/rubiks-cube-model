"""Tests for Rubik's cube move logic."""

import pytest
from cube import Cube


class TestInit:
    """Test cube state initialization."""

    def test_solved_cube_state(self):
        """Verify a new cube starts in solved state."""
        cube = Cube()
        assert cube.state["U"] == ["W"] * 9
        assert cube.state["D"] == ["Y"] * 9
        assert cube.state["F"] == ["F"] * 9
        assert cube.state["B"] == ["B"] * 9
        assert cube.state["L"] == ["O"] * 9
        assert cube.state["R"] == ["R"] * 9


class TestInverse:
    """Test that inverse moves undo forward moves."""

    def test_u_and_u_prime(self):
        """U followed by U' returns to solved state."""
        cube = Cube()
        original = {face: stickers[:] for face, stickers in cube.state.items()}
        
        cube.U()
        cube.U_prime()
        
        for face in original:
            assert cube.state[face] == original[face]

    def test_d_and_d_prime(self):
        """D followed by D' returns to solved state."""
        cube = Cube()
        original = {face: stickers[:] for face, stickers in cube.state.items()}
        
        cube.D()
        cube.D_prime()
        
        for face in original:
            assert cube.state[face] == original[face]

    def test_r_and_r_prime(self):
        """R followed by R' returns to solved state."""
        cube = Cube()
        original = {face: stickers[:] for face, stickers in cube.state.items()}
        
        cube.R()
        cube.R_prime()
        
        for face in original:
            assert cube.state[face] == original[face]

    def test_l_and_l_prime(self):
        """L followed by L' returns to solved state."""
        cube = Cube()
        original = {face: stickers[:] for face, stickers in cube.state.items()}
        
        cube.L()
        cube.L_prime()
        
        for face in original:
            assert cube.state[face] == original[face]

    def test_f_and_f_prime(self):
        """F followed by F' returns to solved state."""
        cube = Cube()
        original = {face: stickers[:] for face, stickers in cube.state.items()}
        
        cube.F()
        cube.F_prime()
        
        for face in original:
            assert cube.state[face] == original[face]

    def test_b_and_b_prime(self):
        """B followed by B' returns to solved state."""
        cube = Cube()
        original = {face: stickers[:] for face, stickers in cube.state.items()}
        
        cube.B()
        cube.B_prime()
        
        for face in original:
            assert cube.state[face] == original[face]


class TestFourMoves:
    """Test that four identical moves return to original state."""

    def test_u_four_times(self):
        """U^4 returns to solved state."""
        cube = Cube()
        original = {face: stickers[:] for face, stickers in cube.state.items()}
        
        for _ in range(4):
            cube.U()
        
        for face in original:
            assert cube.state[face] == original[face]

    def test_d_four_times(self):
        """D^4 returns to solved state."""
        cube = Cube()
        original = {face: stickers[:] for face, stickers in cube.state.items()}
        
        for _ in range(4):
            cube.D()
        
        for face in original:
            assert cube.state[face] == original[face]

    def test_r_four_times(self):
        """R^4 returns to solved state."""
        cube = Cube()
        original = {face: stickers[:] for face, stickers in cube.state.items()}
        
        for _ in range(4):
            cube.R()
        
        for face in original:
            assert cube.state[face] == original[face]

    def test_l_four_times(self):
        """L^4 returns to solved state."""
        cube = Cube()
        original = {face: stickers[:] for face, stickers in cube.state.items()}
        
        for _ in range(4):
            cube.L()
        
        for face in original:
            assert cube.state[face] == original[face]

    def test_f_four_times(self):
        """F^4 returns to solved state."""
        cube = Cube()
        original = {face: stickers[:] for face, stickers in cube.state.items()}
        
        for _ in range(4):
            cube.F()
        
        for face in original:
            assert cube.state[face] == original[face]

    def test_b_four_times(self):
        """B^4 returns to solved state."""
        cube = Cube()
        original = {face: stickers[:] for face, stickers in cube.state.items()}
        
        for _ in range(4):
            cube.B()
        
        for face in original:
            assert cube.state[face] == original[face]


class TestSequences:
    """Test common move sequences and their effects."""

    def test_sexy_move(self):
        """R U R' U' sequence is a common speedcubing algorithm."""
        cube = Cube()
        original = {face: stickers[:] for face, stickers in cube.state.items()}
        
        # Sexy move
        cube.R()
        cube.U()
        cube.R_prime()
        cube.U_prime()
        
        # After one sexy move, cube should be different
        assert any(cube.state[face] != original[face] for face in original)
        
        # Six sexy moves should return to solved
        for _ in range(5):  # We already did one
            cube.R()
            cube.U()
            cube.R_prime()
            cube.U_prime()
        
        for face in original:
            assert cube.state[face] == original[face]

    def test_move_sequence_affects_multiple_faces(self):
        """Moves should affect appropriate faces."""
        cube = Cube()
        original = {face: stickers[:] for face, stickers in cube.state.items()}
        cube.R()
        
        # R move affects: U, F, D, B right columns and R face (rotation only)
        # Since solved cube has all same color on R, check that edge stickers moved
        assert (cube.state["U"][2] != original["U"][2] or 
                cube.state["U"][5] != original["U"][5] or 
                cube.state["U"][8] != original["U"][8])  # Right column of U changed