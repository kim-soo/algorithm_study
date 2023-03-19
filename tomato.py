from collections import deque

m, n = map(int, input().split())

box = []

for i in range(n):
    box.append(list(map(int, input().split())))


queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j]==1:
            queue.append([i,j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
def bfs():

    while queue:
        x,y = queue.popleft()

        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny <0 or ny >=m:
                continue
            elif box[nx][ny] == 0:
                box[nx][ny] = box[x][y] +1
                queue.append([nx, ny])

bfs()
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))

print(result-1)