import numpy as np

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [list(line.rstrip("\n")) for line in file if line.rstrip("\n")]

def count_accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    accessible = 0
    out_grid = [row.copy() for row in grid]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue
            neigh = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        neigh += 1
            if neigh < 4:
                accessible += 1
                out_grid[r][c] = 'x'
    return accessible, out_grid

if __name__ == "__main__":
    grid = read_input('day4/input.txt')
    accessible, marked = count_accessible_rolls(grid)
    print(accessible)