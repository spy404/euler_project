import os


def largest_product(grid):
    n_columns = len(grid[0])
    n_rows = len(grid)

    largest = 0
    lr_diag_product = 0
    rl_diag_product = 0

    for i in range(n_columns):
        for j in range(n_rows - 3):
            vert_product = grid[j][i] * grid[j + 1][i] * grid[j + 2][i] * grid[j + 3][i]
            horz_product = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]

            if i < n_columns - 3:
                lr_diag_product = (
                    grid[i][j]
                    * grid[i + 1][j + 1]
                    * grid[i + 2][j + 2]
                    * grid[i + 3][j + 3]
                )

            if i > 2:
                rl_diag_product = (
                    grid[i][j]
                    * grid[i - 1][j + 1]
                    * grid[i - 2][j + 2]
                    * grid[i - 3][j + 3]
                )

            max_product = max(
                vert_product, horz_product, lr_diag_product, rl_diag_product
            )
            if max_product > largest:
                largest = max_product

    return largest


def solution():
    grid = []
    with open(os.path.dirname(__file__) + "/grid.txt") as file:
        for line in file:
            grid.append(line.strip("\n").split(" "))

    grid = [[int(i) for i in grid[j]] for j in range(len(grid))]

    return largest_product(grid)

print(solution())
