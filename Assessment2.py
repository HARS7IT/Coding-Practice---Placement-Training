import random
import time
import os

width, height = 20, 10

snake = [[5, 5], [5, 4], [5, 3]]  # snake body positions
food = [random.randint(1, height-2), random.randint(1, width-2)]

direction = "RIGHT"

def print_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    for r in range(height):
        row = ""
        for c in range(width):
            if [r, c] == food:
                row += "*"
            elif [r, c] in snake:
                row += "O"
            else:
                row += "."
        print(row)

while True:
    print_board()

    move = input("Move (w/a/s/d): ").lower()

    if move == "w":
        direction = "UP"
    elif move == "s":
        direction = "DOWN"
    elif move == "a":
        direction = "LEFT"
    elif move == "d":
        direction = "RIGHT"

    head = snake[0].copy()

    if direction == "UP":
        head[0] -= 1
    elif direction == "DOWN":
        head[0] += 1
    elif direction == "LEFT":
        head[1] -= 1
    elif direction == "RIGHT":
        head[1] += 1

    if head in snake or head[0] < 0 or head[0] >= height or head[1] < 0 or head[1] >= width:
        print("Game Over!")
        break

    snake.insert(0, head)

    if head == food:
        food = [random.randint(1, height-2), random.randint(1, width-2)]
    else:
        snake.pop()

    time.sleep(0.1)
