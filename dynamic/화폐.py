n, m = map(int, input().split())

money = []

for _ in range(n):
    money.append(int(input()))

lst = [ 10001 * (m+1) ]

lst[0] = 0

for x in range (n):
    for y in range(money[x], m+1):
        if lst[x - money[y]] != 10001:
            lst[x] = min(lst[x-money[y]]+1, lst[x])


if lst[m] == 10001:
    print (-1)
else :
    print (lst[m])