import sys


x, y = 0, 0

n = int(sys.stdin.readline())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]



for i in range(n):
    dir, dist = input().split()
    dist = int(dist)

    if dir == 'N':
        # y += dist
        dir_num = 0
    elif dir == 'E':
        # x += dist
        dir_num = 1
    elif dir == 'S':
        # y -= dist
        dir_num = 2
    else:
        # x -= dist
        dir_num = 3
    
    x += dist * dx[dir_num]
    y += dist * dy[dir_num]
    
print(x, y)