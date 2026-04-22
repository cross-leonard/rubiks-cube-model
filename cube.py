

class Cube:
    def __init__(self):
        self.state = {
            "U": ["W"] * 9,
            "D": ["Y"] * 9,
            "F": ["0", "F", "0", "F", "F", "F", "F", "F", "F"],
            "B": ["B"] * 9,
            "L": ["O"] * 9,
            "R": ["R"] * 9
        }

    def _cycle_indices_clockwise(self, face1: str, indices1: list[int], face2: str, indices2: list[int], face3: str, indices3: list[int], face4: str, indices4: list[int]) -> None:
        """Clockwise 4-way cycle for strips that are not simple slices."""
        temp = [self.state[face1][index] for index in indices1]

        for i in range(len(indices1)):
            target_index = indices1[i]
            source_index = indices4[i]
            self.state[face1][target_index] = self.state[face4][source_index]

        for i in range(len(indices4)):
            target_index = indices4[i]
            source_index = indices3[i]
            self.state[face4][target_index] = self.state[face3][source_index]
        
        for i in range(len(indices3)):
            target_index = indices3[i]
            source_index = indices2[i]
            self.state[face3][target_index] = self.state[face2][source_index]
        
        for i in range(len(indices2)):
            target_index = indices2[i]
            self.state[face2][target_index] = temp[i]

    def _rotate_face_clockwise(self, face: str) -> None:
        old = self.state[face][:]
        self.state[face][0] = old[6]
        self.state[face][1] = old[3]
        self.state[face][2] = old[0]
        self.state[face][3] = old[7]
        self.state[face][4] = old[4]
        self.state[face][5] = old[1]
        self.state[face][6] = old[8]
        self.state[face][7] = old[5]
        self.state[face][8] = old[2]

    def U(self) -> None:
        self._cycle_indices_clockwise("F", [0, 1, 2], "L", [0, 1, 2], "B", [0, 1, 2], "R", [0, 1, 2])
        self._rotate_face_clockwise("U")

    def D(self) -> None:
        self._cycle_indices_clockwise("F", [6, 7, 8], "R", [6, 7, 8], "B", [6, 7, 8], "L", [6, 7, 8])
        self._rotate_face_clockwise("D")

    def R(self) -> None:
        self._cycle_indices_clockwise("U", [2, 5, 8], "B", [6, 3, 0], "D", [2, 5, 8], "F", [2, 5, 8])
        self._rotate_face_clockwise("R")

    def L(self) -> None:
        self._cycle_indices_clockwise("U", [0, 3, 6], "F", [0, 3, 6], "D", [0, 3, 6], "B", [8, 5, 2])
        self._rotate_face_clockwise("L")

    def F(self) -> None:
        self._cycle_indices_clockwise("U", [6, 7, 8], "R", [0, 3, 6], "D", [0, 1, 2], "L", [2, 5, 8])
        self._rotate_face_clockwise("F")

    def B(self) -> None:
        self._cycle_indices_clockwise("U", [0, 1, 2], "L", [0, 3, 6], "D", [6, 7, 8], "R", [2, 5, 8])
        self._rotate_face_clockwise("B")

    def U_prime(self) -> None:
        for _ in range(3):
            self.U()

    def D_prime(self) -> None:
        for _ in range(3):
            self.D()

    def R_prime(self) -> None:
        for _ in range(3):
            self.R()

    def L_prime(self) -> None:
        for _ in range(3):
            self.L()

    def F_prime(self) -> None:
        for _ in range(3):
            self.F()

    def B_prime(self) -> None:
        for _ in range(3):
            self.B()


