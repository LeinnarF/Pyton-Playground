# Conway's Game of Life mini implementation in Python
'''

Set up:
1. a 5x5 grid with some initial live cells.
2. define rules for cell survival, death, and birth.
3. 1 = live cell, 0 = dead cell.

Rules:
- Any live cell with two or three live neighbours survives.
- Any dead cell with exactly three live neighbours becomes a live cell.


'''

generations = 5

init_grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
]

def PrintGrid(grid):
    for row in grid:
        print(' '.join(str(cell) for cell in row))
    print()

# Check neighbors
def NeighborCount(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            count += grid[nx][ny]
    return count

def NextGeneration(current_grid):
    new_grid = [[0 for _ in range(len(current_grid[0]))] for _ in range(len(current_grid))]
    
    for i in range(len(current_grid)):
        
        for j in range(len(current_grid[0])):

            neighbors = NeighborCount(current_grid, i, j)

            if current_grid[i][j] == 1:
                if neighbors in [2, 3]:
                    new_grid[i][j] = 1
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid

current_grid = init_grid
print("Initial Generation:")
PrintGrid(current_grid)

for gen in range(generations):
    current_grid = NextGeneration(current_grid)
    print(f"Generation {gen + 1}:")
    PrintGrid(current_grid)