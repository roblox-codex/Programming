MAX_GRID_SIZE = 25

# Define an enum class to represent the different directions.
class direction_t:
    DIR_RIGHT = 0
    DIR_DOWN = 1
    DIR_LEFT = 2
    DIR_UP = 3

# Define a function to print the current grid state.
def print_grid(grid, n):
    print("Current Grid State:")
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=' ')
        print()
    print()

# Define a function to clean a single tile.
def clean_tile(grid, i, j):
    grid[i][j] = 0

# Define the main function to clean the entire grid.
def clean_grid(grid, n):
    # Start from the top left corner facing right.
    i, j = 0, 0
    direction = direction_t.DIR_RIGHT
    while True:
        # Clean the current tile and print the grid state.
        clean_tile(grid, i, j)
        print_grid(grid, n)
        
        # Check if all tiles are clean.
        all_clean = all(grid[x][y] == 0 for x in range(n) for y in range(n))
        if all_clean:
            print("All tiles are clean.")
            return
        
        # Move in the current direction.
        if direction == direction_t.DIR_RIGHT:
            # If at right edge, change direction and move down.
            if j == n-1:
                direction = direction_t.DIR_DOWN
                i += 1
            else:
                j += 1
        elif direction == direction_t.DIR_DOWN:
            # If at bottom edge, change direction and move left.
            if i == n-1:
                direction = direction_t.DIR_LEFT
                j -= 1
            else:
                i += 1
        elif direction == direction_t.DIR_LEFT:
            # If at left edge, change direction and move up.
            if j == 0:
                direction = direction_t.DIR_UP
                i -= 1
            else:
                j -= 1
        elif direction == direction_t.DIR_UP:
            # If at top edge, change direction and move right.
            if i == 0:
                direction = direction_t.DIR_RIGHT
                j += 1
            else:
                i -= 1

# Set the size of the grid and initialize all tiles as dirty.
n = 5
grid = [[1 for j in range(n)] for i in range(n)]

# Clean the grid using the goal-based agent.
clean_grid(grid, n)
