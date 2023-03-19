n, m = map(int, input().split())

tray = []
for i in range(n):
    tray.append(list(map(int, input())))

def makeice(x, y):
    if x<0 or x >=n or y < 0 or y >= m:
        return False
    elif tray[x][y] == 0:
        tray[x][y] = 1
        makeice(x, y-1)
        makeice(x+1, y)
        makeice(x-1, y)
        makeice(x, y+1)
        return True

    return False

result = 0

for i in range(n):
    for j in range(m):
        if makeice(i, j) == True:
            result +=1

print (result)
    