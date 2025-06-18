import sys

from main import pars_args, pars_grid, get_start
from puzzle import Puzzle


def main():
    args = pars_args()
    grid = pars_grid(args.file)
    row, col = get_start(grid)
    goal = Puzzle.get_goal(len(grid))
    puzzle = Puzzle(grid, row, col)
    for line in sys.stdin:
        line = line[:-1]
        puzzle = Puzzle.execute(puzzle, line)
    print(puzzle)
    print(puzzle == goal)


if __name__ == "__main__":
    # try:
    main()
# except Exception as error:
#     print(type(error).__name__ + ":", error)
