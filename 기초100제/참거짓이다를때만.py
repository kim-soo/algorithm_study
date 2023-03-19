c, d= map(bool, (map(int, input().split())))

print ((c and (not d) or (not c) and d))