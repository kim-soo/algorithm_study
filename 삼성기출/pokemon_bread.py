n, m = int(input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
store = [list(map(int, input().split())) for _ in range(m)]

x = [-1, 0, 0, 1]
y = [0, -1, 1, 0]

def basecamp ():
