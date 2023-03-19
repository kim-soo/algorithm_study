N = int(input())
T = []
P = []
for i in range(N):
    temp = list(map(int, input().split()))
    T.append(temp[0])
    P.append(temp[1])

dp = [ 0 for i in range(N+1) ]

for i in range(N-1, -1, -1):
    if T[i] + i <= N:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i+1])
    else :
        dp[i] = dp[i+1]

print(dp[0])