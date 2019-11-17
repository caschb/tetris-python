from copy import deepcopy
from typing import Dict, List


class Piece:
    ZSHAPE: List[List[int]] = [[0, -1], [0, 0], [-1, 0], [-1, 1]]
    SSHAPE: List[List[int]] = [[0, -1], [0, 0], [1, 0], [1, 1]]
    ISHAPE: List[List[int]] = [[0, -1], [0, 0], [0, 1], [0, 2]]
    TSHAPE: List[List[int]] = [[-1, 0], [0, 0], [1, 0], [0, 1]]
    SQUARE: List[List[int]] = [[0, 0], [0, 1], [1, 0], [1, 1]]
    LSHAPE: List[List[int]] = [[-1, -1], [0, -1], [0, 0], [0, 1]]
    JSHAPE: List[List[int]] = [[1, -1], [0, -1], [0, 0], [0, 1]]

    SHAPES: List[List[List[int]]] = [ZSHAPE, SSHAPE, ISHAPE, TSHAPE, SQUARE, LSHAPE, JSHAPE]

    SHAPE_NAMES: Dict[str, int] = {
        'ZShape': 0,
        'SShape': 1,
        'IShape': 2,
        'TShape': 3,
        'Square': 4,
        'LShape': 5,
        'JShape': 6
    }

    SHAPE_NUM: int = len(SHAPES)

    def __init__(self, shape_idx: int = -1):
        self.position = None
        self.my_shape = None
        self.shape_type: int = shape_idx

        if self.shape_type != -1:
            self.set_piece(self.shape_type)

    def set_piece(self, shape_idx: int):
        self.shape_type = shape_idx
        self.my_shape = Piece.SHAPES[shape_idx]
        self.reset()

    def reset(self):
        self.position = deepcopy(self.my_shape)
