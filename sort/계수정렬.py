n = list(map(int, input().split()))

count = [0] * (max(n)+1)

for i in range(len(n)):
    count[n[i]] +=1

for j in range(len(count)):
    for k in range(count[j]):
        print(j, end=' ')