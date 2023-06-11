from random import randint
import curses

# globals
ESC_KEY = 27

# intialize curses
curses.initscr()

curses.noecho()
curses.curs_set(0)

win = curses.newwin(20, 60, 0, 0)
win.keypad(True)
win.border(0)
win.nodelay(1)

# intial states of snake and food
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)

win.addch(food[0], food[1], '#')

# game logic
score = 0
key = curses.KEY_RIGHT

while key != ESC_KEY:
    win.addstr(0, 2, ' Score: ' + str(score) + ' ')
    win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120)  # increases snake speed

    prev_key = key
    event = win.getch()

    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC_KEY]:
        key = prev_key

    # calculating new snake state
    y = snake[0][0]
    x = snake[0][1]

    if key == curses.KEY_DOWN:
        y += 1
    elif key == curses.KEY_UP:
        y -= 1
    elif key == curses.KEY_LEFT:
        x -= 1
    elif key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x))

    # Checking if Snake Hit the Borders
    if y == 0:
        break
    if y == 19:
        break
    if x == 0:
        break
    if x == 59:
        break

    # checking if the snake collided into itself
    if snake[0] in snake[1:]:
        break

    # checking if the snake ate food
    if snake[0] == food:
        score += 100

        # creating new food and showing it
        food = ()

        while food == ():
            food = (randint(1, 18), randint(1, 58))

            if food in snake:
                food = ()

        win.addch(food[0], food[1], '#')

    else:
        # moving the snake
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(snake[0][0], snake[0][1], '█')

curses.endwin()
print(f'Game over!\nYour score was: {score}')
