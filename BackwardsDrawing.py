#!/usr/bin/env python
##########################################
#          Rotate the heart 90°          #
##########################################

__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"

grid =   [['.', '.', '.', '.', '.', '.'],
          ['.', 'O', 'O', '.', '.', '.'],
          ['O', 'O', 'O', 'O', '.', '.'],
          ['O', 'O', 'O', 'O', 'O', '.'],
          ['.', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', '.'],
          ['O', 'O', 'O', 'O', '.', '.'],
          ['.', 'O', 'O', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.']]

# Normal heart
print("\nNormal heart:\n")

for i in range(6):
    for a in range(9):
        if a < 8:
            print(grid[a][i], end="")
        else:
            print(grid[a][i])

# Rotated
print("\nRotated:\n")
for i in range(6):
    for a in range(9):
        if a < 8:
            print(grid[a][-(i+1)], end="")
        else:
            print(grid[a][i])
