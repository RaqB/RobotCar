from turtle import *
from MyGraph import MyGraph

redLines = True
maze = MyGraph({
    50: (-1, 30, -1, -1),
    30: (32, -1, -1, 50),
    32: (33, 12, 30, -1),
    33: (-1, -1, 32, 53),
    53: (54, 33, 51, -1),
    51: (53, 41, -1, -1),
    41: (42, -1, -1, 51),
    42: (-1, -1, 41, -1),
    54: (-1, 34, 53, -1),
    34: (35, -1, -1, 54),
    35: (-1, -1, 34, 55),
    55: (-1, 35, -1, -1),
    12: (13, 2, -1, 32),
    13: (-1, -1, 12, -1),
    2: (4, -1, 1, 12),
    4: (-1, -1, 2, 24),
    24: (25, 4, 23, -1),
    23: (24, -1, -1, -1),
    25: (-1, 5, 24, -1),
    5: (-1, -1, -1, 25),
    1: (2, -1, -1, 21),
    21: (-1, 1, 20, -1),
    20: (21, 0, -1, -1),
    0: (-1, -1, -1, 20)
})


def stop():
    left(90)
    done()


def toCoord(node):
    f, c = node // 10, node % 10
    return -210 + (84 * c), 210 + (-84 * f)


def fly(x, y=None):
    penup()
    goto(x, y)
    pendown()


def drawPaths(node):
    maze[node] = False
    for ch in maze[node]:
        if ch != -1 and maze.isenabled(ch):
            fly(toCoord(node))
            goto(toCoord(ch))
            dot(5, 'black')
            if redLines:
                pen(pencolor='black')
            write("{} {}".format(ch // 10, ch % 10),
                  align="center", font=("Consolas", 12, "bold"))
            if redLines:
                pen(pencolor='red')
            drawPaths(ch)
            dot(15, '#33ff99')


def drawMaze(start=50):
    # { frame
    fly(-252, 252)
    pensize(5)
    for i in range(4):
        forward(504)
        right(90)
    # }
    pensize(1)
    # {	colums and row
    for i in range(-168, 252, 84):
        left(90)
        fly(i, -252)
        forward(504)
        right(90)
        fly(-252, i)
        forward(504)
    # }
    fly(toCoord(start))
    write("{} {}".format(start // 10, start % 10),
          align="center", font=("Consolas", 12, "bold"))
    dot(15, '#9999ff')
    if redLines:
        pen(pencolor='red', pensize=2)
    drawPaths(start)
    if redLines:
        pen(pencolor='black')
    fly(toCoord(start))
    dot(15, '#9999ff')

if __name__ == '__main__':
    setup(1000, 800)  # width, height
    speed(10)
    shapesize(0.8, 0.8, 0.3)
    drawMaze()
    stop()
