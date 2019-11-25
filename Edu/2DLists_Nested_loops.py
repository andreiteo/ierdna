#!/usr/local/bin/python3
import sys
print(sys.version)


number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#aici specifici sa printeze indexul 0 pentru randul zero si apoi indexul 0 pentru coloana zero
print(number_grid[0][0])


print(number_grid[1][1])



for rows in number_grid:
    for column in rows:
        print(column)
