n = int(input())
m = list(map(int, input().split()))

def adventure(m):
    m.sort()
    cnt = 0
    crew=0
    for i in m:
        crew += 1
        if crew >= i:
            cnt += 1
            crew = 0

    return cnt


print(adventure(m))