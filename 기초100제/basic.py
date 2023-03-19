n = int(input())

cnt = 0
for i in range(1000):
    cnt += i
    if cnt > n:
        print(i-1)
        break