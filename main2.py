import random


grid = []

for i in range(36):
    grid.append(0)

apple = int(random.random() * 35)

snake = int(random.random() * 35)
print(len(grid))
while snake == apple and snake >= len(grid) and apple >= len(grid):
    snake = int(random.random() * 35)

grid.pop(apple)
grid.insert(apple, 'x')
grid.pop(snake)
grid.insert(snake, 's')

def game():
    for i in range(6, 36, 6):
        print(*grid[i-6:i])
    ind = grid.index('s')
    app = grid.index('x')
    while ind != app:
        move = input('enter move: ')

        if move == 'up':
            grid.pop(ind)
            grid.insert(ind-6, 's')
            # grid.insert(ind-1, 0)
        for i in range(6, 36, 6):
            print(*grid[i-6:i])


while True:
    game()


        

# for i in range(6):
#     print(grid[i])
# for i in range()