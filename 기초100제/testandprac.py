import sys
from collections import deque

INT_MAX = sys.maxsize
EMPTY = (-1, -1)

n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

cv_stores = []
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    cv_stores.append((x - 1, y - 1))

people = [EMPTY] * m
cur_time = 0
step = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def can_visit(x, y):
    return 0 <= x < n and 0 <= y < n and visited[x][y] == 0 and grid[x][y] !=2

def bfs(start):
    for i in range(n):
        for j in range(n):
            step[i][j] = 0
            visited[i][j] = 0
    q = deque()
    x, y = start
    q.append([x, y])
    visited[x][y] = 1
    step[x][y] = 0

    while (q):
        x, y = q.popleft()
        for tx, ty in zip(dx, dy):
            nx, ny = x + tx, y + ty
            if can_visit(nx, ny):
                visited[nx][ny] = 1
                step[nx][ny] = step[x][y] + 1
                q.append((nx, ny))

def simulate():
    # 한칸이동
    for idx in range(m):
        if people[idx] == EMPTY or people[idx] == cv_stores[idx]:
            continue
        min_dist = INT_MAX
        pur_x, pur_y = -1, -1
        x, y = people[idx]
        bfs(cv_stores[idx])
        for ti, tj in zip(dx, dy):
            ni, nj = x + ti, y + tj
            if (in_range(ni, nj)):
                if (visited[ni][nj] and step[ni][nj] < min_dist):
                    min_dist = step[ni][nj]
                    pur_x, pur_y = ni, nj

        people[idx] = (pur_x, pur_y)

        if people[idx] == cv_stores[idx]:
            x, y = people[idx]
            grid[x][y] = 2

    if cur_time <= m:
        min_dist = INT_MAX
        pur_i, pur_j = -1, -1
        bfs(cv_stores[cur_time-1])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] and step[i][j] < min_dist:
                    min_dist = step[i][j]
                    pur_i, pur_j = i, j

        people[cur_time - 1] = (pur_i, pur_j)
        grid[pur_i][pur_j] = 2
    else : return

def end():
    for i in range(m):
        if people[i] != cv_stores[i]:
            return False
    return True

while True:
    cur_time += 1
    simulate()
    if end():
        break

print(cur_time)