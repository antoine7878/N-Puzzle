import heapq
import math
from heuristic import Manhattan, Heuristic

from puzzle import Puzzle


class Solver:
    def __init__(
        self,
        start: Puzzle,
        heuristic: Heuristic = Manhattan(),
        quiet: bool = False,
    ) -> None:
        self.size = int(math.sqrt(len(start.grid)))
        self.goal, self.goal_list = Puzzle.get_goal(self.size)
        self.open = [start]
        self.openDict = {start.grid: [start]}
        self.closed = set()
        self.start = start
        self.heuristic: Heuristic = heuristic
        self.start.g = 0
        self.start.f = self.heuristic(self.start, self.goal_list)
        self.tot_open = 0
        self.max_open = 0
        self.quiet = quiet

    def solve(self) -> None:
        while self.open:
            current = heapq.heappop(self.open)
            if len(self.openDict[current.grid]) == 1:
                del self.openDict[current.grid]
            if current == self.goal:
                return self.print_solution(current)
            self.closed.add(current.grid)
            neighbours = [
                Puzzle.execute(current, action) for action in Puzzle.actions
            ]
            for next in neighbours:
                if not next or next.grid in self.closed:
                    continue

                next.g = current.g + 1
                if next.grid not in self.openDict:
                    self.tot_open += 1
                    self.max_open = max(self.max_open, len(self.open))
                    next.f = next.g + self.heuristic(next, self.goal_list)
                    heapq.heappush(self.open, next)
                    self.openDict[next.grid] = [next]
                elif next.g < self.openDict[next.grid][-1].g:
                    self.tot_open += 1
                    self.max_open = max(self.max_open, len(self.open))
                    heapq.heappush(self.open, next)
                    next.f = next.g + self.heuristic(next, self.goal_list)
                    self.openDict[next.grid].append(next)
        print("The puzzle in not solvable")

    def print_solution(self, node: Puzzle):
        cur = node
        solution = []
        while cur:
            solution.insert(0, cur.parent_dir)
            cur = cur.parent
        for move in solution[1:]:
            print(move)
        if not self.quiet:
            print("Number of move:", len(solution) - 1)
            print("Total selected states:", self.tot_open)
            print("Maximum selected states:", self.max_open)
