n = int(input())
k = list(map(int, input().split()))

m = [ 0 for i in range(n)]
m[0] = k[0]
m[1] = max(k[0], k[1])

for x in range(2, n):
    m[x] = max(k[x] + k[x-2], k[x-1])

print(m[n-1])