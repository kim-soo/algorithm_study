from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
x, y, size = 0, 0, 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j

def eatFish(x, y, shark_size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    

# bfs 사용하여 탐색
while 1:
    eatFish(x, y, size)