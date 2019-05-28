maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


# 判断当前位置是否为通路
def ispass(maze, pos):
    return maze[pos[0]][pos[1]] == 0


# 探测过的路标记为2
def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2


path = []  # 保存通路的节点的坐标

# 向上探测 y=y-1  左：x=x-1  下  y=y+1   右 x=x+1
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 探测顺序  上右下左


def find_path(maze, pos, end):  # 三个参数：地图；入口；出口
    mark(maze, pos)
    if pos == end:  # 判断是否只有一个节点，即入口就是出口
        path.append(pos)
        return True
    for i in range(4):  # 循环探测四个方向
        next = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
        if ispass(maze, next):  # 如果当前元素为0，递归调用find_path
            if find_path(maze, next, end):
                path.append(pos)
                return True
    return False


find_path(maze, (1, 1), (10, 10))

for item in path:
    maze[item[0]][item[1]] = 3

# 循环输出元素，不同的元素用不同的颜色表示
for y in maze:
    for x in y:
        if x == 1:
            print("\033[0;41;m" + str(x) + "\033[0m", end=" ")
        elif x == 2:
            print("\033[0;42;m" + str(x) + "\033[0m", end=" ")
        elif x == 3:
            print("\033[0;43;m*\033[0m", end=" ")
        else:
            print("\033[0;;m" + str(x) + "\033[0m", end=" ")
    print()


