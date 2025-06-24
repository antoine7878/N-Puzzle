import math
from abc import ABC, abstractmethod

from puzzle import Puzzle


class Heuristic(ABC):
    @abstractmethod
    def __call__(self, state: Puzzle, goal_list: list) -> float:
        return -1


class Euclide(Heuristic):
    def __call__(self, state: Puzzle, goal_list: list) -> float:
        tot = 0
        for i, val in enumerate(state.grid):
            if val:
                row_goal, col_goal = goal_list[val]
                row = i // state.size
                col = i % state.size
                tot += math.sqrt((row_goal - row) ** 2 + (col_goal - col) ** 2)
        return int(tot)


class Manhattan(Heuristic):
    def __call__(self, state: Puzzle, goal_list: list) -> float:
        tot = 0
        for i, val in enumerate(state.grid):
            if val:
                row_goal, col_goal = goal_list[val]
                row = i // state.size
                col = i % state.size
                tot += abs(row_goal - row) + abs(col_goal - col)
        return tot


class Misplaced(Heuristic):
    def __call__(self, state: Puzzle, goal_list: list) -> float:
        tot = 0
        for i, val in enumerate(state.grid):
            if val:
                row = i // state.size
                col = i % state.size
                if val and (row, col) == goal_list[val]:
                    tot += 1
        return tot


heuristics = [Manhattan, Euclide, Misplaced]
