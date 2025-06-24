import math


class Puzzle:
    actions_to_move = {
        "TOP": (-1, 0),
        "RIGHT": (0, 1),
        "BOTTOM": (1, 0),
        "LEFT": (0, -1),
    }
    actions = ["LEFT", "RIGHT", "TOP", "BOTTOM"]

    def __init__(
        self,
        grid: tuple,
        row: int,
        col: int,
        parent=None,
        parent_dir: str | None = None,
    ) -> None:
        self.grid: tuple = grid
        self.size: int = int(math.sqrt(len(grid)))
        self.row: int = row
        self.col: int = col
        self.g: float = 0
        self.f: float = 0
        self.parent: Puzzle | None = parent
        self.parent_dir: str | None = parent_dir

    def __str__(self) -> str:
        ret = ""
        for row in self.grid:
            for cell in row:
                ret += str(cell)
                if cell == row[-1]:
                    continue
                if cell < 10:
                    ret += "  "
                else:
                    ret += " "
            if row != self.grid[-1]:
                ret += "\n"
        return ret

    def __hash__(self) -> int:
        return hash(self.grid)

    def __eq__(self, other):
        return self.grid == other.grid

    def __lt__(self, other):
        return self.f < other.f

    @classmethod
    def execute(cls, src, action: str):
        new_row = src.row + Puzzle.actions_to_move[action][0]
        if not -1 < new_row < src.size:
            return None

        new_col = src.col + Puzzle.actions_to_move[action][1]
        if not -1 < new_col < src.size:
            return None

        new_pos = new_row * src.size + new_col
        zero_pos = src.row * src.size + src.col

        new_grid = list(src.grid)
        new_grid[zero_pos] = new_grid[new_pos]
        new_grid[new_pos] = 0

        return cls(tuple(new_grid), new_row, new_col, src, action)

    @staticmethod
    def next_snail(row, col, dir_row, dir_col, start, end):
        if col == end and dir_col == 1:
            dir_row = 1
            dir_col = 0
        elif row == end and dir_row == 1:
            dir_row = 0
            dir_col = -1
            end -= 1
        elif col == start and dir_col == -1:
            dir_row = -1
            dir_col = 0
            start += 1
        elif row == start and dir_row == -1:
            dir_row = 0
            dir_col = 1
        return row + dir_row, col + dir_col, dir_row, dir_col, start, end

    @classmethod
    def get_goal(cls, size: int) -> tuple:
        grid = [[0 for _ in range(size)] for _ in range(size)]
        col = 0
        row = 0
        dir_row = 0
        dir_col = 1
        end = size - 1
        start = 0
        goal_list = [(-1, -1)]
        for i in range(1, size**2):
            goal_list.append((row, col))
            grid[row][col] = int(i)
            row, col, dir_row, dir_col, start, end = Puzzle.next_snail(
                row, col, dir_row, dir_col, start, end
            )
        grid = tuple(v for row in grid for v in row)
        goal = cls(grid, size - 1, size - 1)
        return goal, goal_list

    @staticmethod
    def get_start(grid) -> tuple[int, int]:
        size = int(math.sqrt(len(grid)))
        for i, val in enumerate(grid):
            if val == 0:
                return i // size, i % size
        raise OverflowError("start not found")
