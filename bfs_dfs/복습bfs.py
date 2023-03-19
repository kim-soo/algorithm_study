from collections import deque

n,m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input())))

vec = [(0,-1), (1, 0), (-1, 0), (0, 1)]

def escape(x, y):
    locate = deque()
    locate.append((x, y))
    while locate:
        x, y = locate.popleft()
        for i in vec:
            nx = x + i[0]
            ny = y + i[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif maze[nx][ny] == 1:
                locate.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
            else: continue

    return maze[n-1][m-1]

print(escape(0, 0))