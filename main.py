import solver

if __name__ == '__main__':

    grid = input("Enter the grid")
    if solver.solveSudoku(grid) is True:
        for row in grid :
            print(row)
