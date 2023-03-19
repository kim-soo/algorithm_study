t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    graph = []
    for _ in range(n):
        graph.append([0]*m)
    for i in range(n):
        for j in range(m):
            graph[i][j] = temp[j+(i*m)]
    for j in range (1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = graph[i-1][j-1]
            if i==n-1:
                left_down = 0
            else: left_down = graph[i+1][j-1]
            left = graph[i][j-1]
            graph[i][j] = graph[i][j] + max(left_up, left_down, left)
    
    result = 0
    for i in range(n):
        result = max(result, graph[i][m-1])
    print(result)