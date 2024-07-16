import random

grid = []


for row in range(6):
    grid.append([])
    for column in range(6):
        grid[row].append(0)
        
row = int(random.random() * 5)
column = int(random.random() * 5)
grid[row].pop(column)
grid[row].insert(column, 'x')
apple = (row, column)

row2 = int(random.random() * 5)
col2 = int(random.random() * 5)
while col2 != column:
    col2 = int(random.random() * 5)
grid[row2].pop(col2)
grid[row2].insert(col2, 's')


def game():
    for row in range(len(grid)):
        print(grid[row])    
        move = input('Enter move: ')
        if move == 'up':
            for row in grid:
                # if grid[row]:
                print(grid[row])


game()