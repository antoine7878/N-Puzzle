import heapq
from heuristic import Manhattan, Heuristic

from puzzle import Puzzle


class Solver:
    def __init__(
        self,
        start: Puzzle,
        heuristic: Heuristic = Manhattan(),
        quiet: bool = False,
    ) -> None:
        self.size = len(start.grid)
        self.goal, self.goal_list = Puzzle.get_goal(self.size)
        self.open = [start]
        self.open_dict = {start.grid: start}
        self.closed = set()
        self.start = start
        self.heuristic: Heuristic = heuristic
        self.start.g = 0
        self.start.h = self.heuristic(self.start, self.goal_list)
        self.start.f = self.start.g + self.start.h
        self.tot_open = 0
        self.max_open = 0
        self.quiet = quiet

    def solve(self) -> None:
        while self.open:
            current = heapq.heappop(self.open)
            del self.open_dict[current.grid]
            if current == self.goal:
                self.print_solution(current)
                return
            self.closed.add(current)
            neighbours = [
                Puzzle.execute(current, action) for action in Puzzle.actions
            ]
            for neighbor, _ in neighbours:
                if not neighbor or neighbor in self.closed:
                    continue

                assert current.g is not None
                tentative_g = current.g + 1

                if neighbor.grid not in self.open_dict:
                    neighbor.g = tentative_g
                    neighbor.h = self.heuristic(neighbor, self.goal_list)
                    assert neighbor.h is not None
                    neighbor.f = tentative_g + neighbor.h
                    heapq.heappush(self.open, neighbor)
                    self.tot_open += 1
                    self.max_open = max(self.max_open, len(self.open))
                    self.open_dict[neighbor.grid] = neighbor
                elif neighbor.g and tentative_g < neighbor.g:
                    old = self.open_dict[neighbor.grid]
                    assert old.h
                    old.g = tentative_g
                    old.f = tentative_g + old.h
                    old.parent = current
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
            print("Number of move:", len(solution))
            print("Total selected states:", self.tot_open)
            print("Maximum selected states:", self.max_open)
