import itertools

data = list(map(int, input().split()))

combi = list(itertools.combinations(data, 3))
result = 0

for i in combi:
    temp = sum(i)
    result = max(result, temp)

print(result)