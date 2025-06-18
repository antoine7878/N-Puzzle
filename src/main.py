import argparse

from heuristic import heuristics
from solver import Solver
from puzzle import Puzzle


def main():
    args = pars_args()
    grid = pars_grid(args.file)
    row, col = get_start(grid)
    puzzle = Puzzle(grid, row, col)
    solver = Solver(puzzle, heuristic=heuristics[args.d](), quiet=args.q)
    solver.solve()


def pars_args():
    parser = argparse.ArgumentParser(
        prog="NPuzzle", description="42 NPuzzle A* star solver"
    )
    parser.add_argument("file")
    parser.add_argument("-d", type=int, default=0, choices=[0, 1, 2])
    parser.add_argument("-q", action="store_true")
    return parser.parse_args()


def pars_grid(path: str):
    file = open(path, "r")
    grid = []
    for i, line in enumerate(file):
        if i != 0:
            nums = line[:-1].split(" ")
            nums = tuple(int(n) for n in nums if n != "")
            grid.append(nums)
    return tuple(grid)


def get_start(grid) -> tuple[int, int]:
    for row, line in enumerate(grid):
        for col, n in enumerate(line):
            if n == 0:
                return row, col
    raise OverflowError("start not found")


if __name__ == "__main__":
    # try:
    main()
# except Exception as error:
# print(type(error).__name__ + ":", error)
