from simplegraph import *

maze = SimpleGraph({
    50: (30, -1, -1, -1),
    30: (-1, 32, 50, -1),
    32: (12, 33, -1, 30),
    33: (-1, -1, 53, 32),
    53: (33, 54, -1, 51),
    51: (41, 53, -1, -1),
    41: (-1, 42, 51, -1),
    42: (-1, -1, -1, 41),
    54: (34, -1, -1, 53),
    34: (-1, 35, 54, -1),
    35: (-1, -1, 55, 34),
    55: (35, -1, -1, -1),
    12: (2, 13, 32, -1),
    13: (-1, -1, -1, 12),
    2: (-1, 4, 12, 1),
    4: (-1, -1, 24, 2),
    24: (4, 25, -1, 23),
    23: (-1, 24, -1, -1),
    25: (5, -1, -1, 24),
    5: (-1, -1, 25, -1),
    1: (-1, 2, 21, -1),
    21: (1, -1, -1, 20),
    20: (0, 21, -1, -1),
    0: (-1, -1, 20, -1)
})

change = ("FRRL", "LFRR", "RLFR", "RRLF")
points = (50, 42, 55, 13, 23, 5, 0)


def findStrOfMoves(start, goal):
    maze.reset()
    path, node, strOfMoves = [start], start, []
    direction = maze.direction(start)

    while node != goal:
        found = maze[node] = False
        for i, n in enumerate(maze[node]):
            if n != -1 and maze.isenabled(n):
                strOfMoves.append(change[direction][i])
                path.append(n)
                node, direction, found = n, i, True
                break
        if not found:
            strOfMoves.pop()
            path.pop()
            node = path[-1]
            direction = maze.direction(path[-2], path[-1])

    return "-".join(strOfMoves)


if __name__ == '__main__':
    with open("answers.txt", "w", encoding="utf-8") as out:
        try:
            for a in points:
                for b in points:
                    if a != b:
                        print("{0:02d} -> {1:02d}: {2}"
                              .format(a, b, findStrOfMoves(a, b)), file=out)
        except Exception as e:
            print(e)
