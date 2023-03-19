N = 100000

def solve():
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = [int(x) + N for x in input.split()]
        tmp = a * 2 * N + b
        arr.append(tmp)
    arr.sort()
    for item in arr:
        a = item // N * 2
        b = item % (N * 2) 
    print (a-N, b-N)

solve()


