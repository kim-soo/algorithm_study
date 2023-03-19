import sys

# T = int(input())

# for i in range(T):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a+b)

# data = []
# n = int(sys.stdin.readline())
# for i in range(n):
#     data.append(list(map(int, sys.stdin.readline().split())))

# print(data)

n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

print(data)