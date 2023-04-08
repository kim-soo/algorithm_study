# 지도 dfs
# 십자선 반시계 90도 회전
# 나머지 각 영역 시계 90도 회전
# dfs, 회전
# 동서남북 파악
import sys
from collections import deque
from copy import deepcopy
from sys import maxsize

n = int(input())
grid = [ list(map(int, input().split())) for _ in range(n)]
int_max = maxsize
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def can_go(x, y, visited, test_grid, sx, sy):
    return visited[x][y] == 0 and test_grid[x][y] == test_grid[sx][sy]

def circulate(test_grid):
    mid_num = int((n-1)/2) # 시계 90도 시 윗줄부터 맨 오른쪽 줄로 넘긴다고 생각하면됨
    temp_grid = deepcopy(test_grid)
    for i in range(mid_num):
        for j in range(mid_num):
            temp_grid[j][mid_num-1-i] = test_grid[i][j]

    for i in range(mid_num+1, n):
        for j in range(mid_num):
            temp_grid[mid_num+1+j][n-1-i] = test_grid[i][j] # (3, 0), (3, 1) -> (3,1), (4,1)

    for i in range(mid_num):
        for j in range(mid_num+1, n):
            temp_grid[j-(mid_num+1)][n-1-i] = test_grid[i][j] #(0,3), (0,4) -> (0,4) (1,4)

    for i in range(mid_num+1, n):
        for j in range(mid_num+1, n):
            temp_grid[j][n-i+(mid_num)] = test_grid[i][j] #(3,3)(3,4)->(3,4)(4,4)

    for i in range(n): #반시계 90도 시 윗줄부터 왼쪽 줄로 넘긴다고 생각하면 됨
        temp_grid[mid_num][i] = test_grid[i][mid_num]
        temp_grid[n-1-i][mid_num] = test_grid[mid_num][i]
    return temp_grid

def simulate(test_grid):
    group_grid = [list(int_max for _ in range(n)) for _ in range(n)]
    visited = [list(0 for _ in range(n)) for _ in range(n)]
    colors = -1
    for i in range(n):
            for j in range(n):
                if group_grid[i][j] == int_max:
                    colors += 1
                    que = deque()
                    que.append((i,j))
                    while que:
                        sx, sy = que.pop()
                        visited[sx][sy] = 1
                        group_grid[sx][sy] = colors
                        for k in range(4):
                            tx, ty = sx + dxs[k], sy + dys[k]
                            if (in_range(tx, ty)):
                                if can_go(tx, ty, visited, test_grid, sx, sy):
                                    que.append((tx, ty))
    return calc(group_grid, colors, test_grid)

def calc(group_grid, colors, grid):
    score = 0
    color_cnt = count_color(group_grid, colors, grid)
    for i in range(n):
         for j in range(n):
             for dx, dy in zip(dxs, dys):
                nx, ny = dx + i, dy + j
                if in_range(nx,ny):
                    if grid[nx][ny] != grid[i][j]:
                        a = color_cnt[group_grid[i][j]]
                        b = color_cnt[group_grid[nx][ny]]
                        c = grid[i][j]
                        d = grid[nx][ny]
                        score += ( a + b ) * c * d
    return score/2

def count_color(g_grid, colors, grid):
    color_cnt = [ 0 for _ in range(n**2)]
    for i in range(n):
        for j in range(n):
            for color in range(colors+1):
                if g_grid[i][j] == color:
                    color_cnt[color] +=1
    return color_cnt

def execute():
    score = 0
    test_grid = deepcopy(grid)
    for _ in range(4):
        score += simulate(test_grid)
        test_grid = circulate(test_grid)
    print(int(score))
execute()