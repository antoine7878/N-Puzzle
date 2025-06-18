from abc import ABC, abstractmethod

from puzzle import Puzzle


class Heuristic(ABC):
    @abstractmethod
    def __call__(self, state: Puzzle, goal_list: list) -> int:
        return -1


class Euclide(Heuristic):
    def __call__(self, state: Puzzle, goal_list: list) -> int:
        tot = 0
        for row, values in enumerate(state.grid):
            for col, cell in enumerate(values):
                if cell:
                    row_goal, col_goal = goal_list[cell]
                    tot += (
                        (row_goal - row) ** 2 + (col_goal - col) ** 2
                    ) ** 0.5
        return tot


class Manhattan(Heuristic):
    def __call__(self, state: Puzzle, goal_list: list) -> int:
        tot = 0
        for row, values in enumerate(state.grid):
            for col, cell in enumerate(values):
                if cell:
                    row_goal, col_goal = goal_list[cell]
                    tot += abs(row_goal - row) + abs(col_goal - col)
        return tot


class Misplaced(Heuristic):
    def __call__(self, state: Puzzle, goal_list: list) -> int:
        tot = 0
        for row, values in enumerate(state.grid):
            for col, cell in enumerate(values):
                if cell and (row, col) == goal_list[cell]:
                    tot += 1
        return tot


heuristics = [Manhattan, Euclide, Misplaced]
