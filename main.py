import random
import curses

# screen

s = curses.initscr()
curses.curs_set(0)

sh, sw = s.getmaxyx()

w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# snake
snk_x = sw/4
snk_y = sh/2

snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]

# food
food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    # next_key = w.getch()
    # if next_key == -1:
    #     next_key = key
    # elif next_key == curses.KEY_DOWN and key == curses.KEY_UP or \
    #      next_key == curses.KEY_UP and key == curses.KEY_DOWN or \
    #      next_key == curses.KEY_LEFT and key == curses.KEY_RIGHT or \
    #      next_key == curses.KEY_RIGHT and key == curses.KEY_LEFT:
    #      wrong_operation = True
    # else:
    #     wrong_operation = False
    # if wrong_operation:
    #     key = key
    # else:
    #     key = next_key

    # next_key = w.getch()
    # if next_key == -1:
    #     next_key = key
    # elif next_key == curses.KEY_DOWN and key == curses.KEY_UP or \
    #      next_key == curses.KEY_UP and key == curses.KEY_DOWN or \
    #      next_key == curses.KEY_LEFT and key == curses.KEY_RIGHT or \
    #      next_key == curses.KEY_RIGHT and key == curses.KEY_LEFT:
    #     wrong_operation = True
    # else:
    #     wrong_operation = False

    # if wrong_operation:
    #     curses.nocbreak()
    #     s.keypad(False)
    #     curses.echo()
    #     curses.endwin()
    #     print('You lose :(')
    #     break
    # else:
    #     key = next_key
    
    next_key = w.getch()
    if (next_key == -1 or next_key == curses.KEY_DOWN and key == curses.KEY_UP or key == curses.KEY_DOWN and next_key == curses.KEY_UP or next_key == curses.KEY_LEFT and key == curses.KEY_RIGHT or key == curses.KEY_LEFT and next_key == curses.KEY_RIGHT):
        wrong_operation = True
    else:
        wrong_operation = False
    if wrong_operation:
        key = key
    else:
        key = next_key

    # snake losing
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.nocbreak()
        s.keypad(False)
        curses.echo()
        curses.endwin()
        print('You lose :(')
        break
        
    
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    # food
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]

            if nf not in snake:
                food = nf
            else:
                food = None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    try:
        w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
    except:
        print('You lose :(') 