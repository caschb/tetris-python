from typing import Dict, List


class Direction:
    RIGHT: List[int] = [0, 1]
    LEFT: List[int] = [0, -1]
    DOWN: List[int] = [1, 0]

    DIRECTIONS: List[List[int]] = [RIGHT, LEFT, DOWN]

    DIRECTION_NAMES: Dict[str, int] = {
        'Right': 0,
        'Left': 1,
        'Down': 2
    }

    def __init__(self, direction: int):
        self.my_direction = Direction.DIRECTIONS[direction]
