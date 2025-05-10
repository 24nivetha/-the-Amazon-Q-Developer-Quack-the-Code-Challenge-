import os
import sys
import time
import random
import threading
import termios
import tty

duck = "🦆"
obstacle = "|"
ground = "‾"
game_width = 40
jump_height = 2
sleep_time = 0.1

score = 0
duck_y = 0
jumping = False
game_over = False
obstacles = [game_width + 10]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw():
    global score
    clear()
    line = [" "] * game_width
    for pos in obstacles:
        if 0 <= pos < game_width:
            line[pos] = obstacle
    if duck_y == 0:
        line[5] = duck
    else:
        print(" " * 5 + duck)
    print("".join(line))
    print(ground * game_width)
    print(f"Score: {score}")

def update_obstacles():
    global obstacles, game_over, score
    for i in range(len(obstacles)):
        obstacles[i] -= 1
    if obstacles and obstacles[0] < 0:
        obstacles.pop(0)
        score += 1
    if random.randint(1, 10) == 1:
        obstacles.append(game_width)

def check_collision():
    global game_over
    if 5 in obstacles and duck_y == 0:
        game_over = True

def jump():
    global duck_y, jumping
    if jumping or game_over:
        return
    jumping = True
    duck_y = jump_height
    time.sleep(0.3)
    duck_y = 0
    jumping =
