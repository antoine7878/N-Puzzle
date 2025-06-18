# N-Puzzle

**N-Puzzle** is a pathfinding and heuristic search project that consists of solving the classic sliding puzzle (3x3, 4x4, NxN) using the **A\*** algorithm.
The puzzle consists of a board with tiles numbered 1 to N²−1 and one empty space. The objective is to reach the “snail” solution (spiral-ordered layout) by sliding the tiles into the empty space.

```
	5 3 1		1 2 3
	7 8 6	->	8 0 4
	4 2 0		7 6 5
```

```
python ./src/main.py ./grids/solvable-4.txt
```

## ⚙️ Features
- Solves arbitrary N-puzzles or 'taquin' (3×3, 4×4, ...)

- Implementation of the A\* algorithm (or a variant)
- **three admissible heuristic functions**: Manhattan, Euclide, Misplaced
- Detailed solution reporting:
  - Total moves to solve the puzzle
  - Number of states explored (time complexity)
  - Max memory usage (size complexity)
  - Ordered list of states leading to the solution

## 🧠 Learning Objectives
- Implement informed search (A\*) with admissible heuristics
- Analyze and compare heuristic quality
- Design and optimize efficient data structures for search spaces

## 📁 File Format
Puzzle input files must follow this format:
```text
3
1 2 3
4 5 6
7 8 0
