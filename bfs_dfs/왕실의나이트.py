a = input()
m = int(a[1])
n = int(ord(a[0])) - int(ord('a')) + 1 

moves = [(-2, -1), (-2, 1), (1, -2), (-1, -2), (2, -1), (2, 1), (1, 2), (-1, 2)]
result = 0

for move in moves :
    next_row = move[0]
    next_col = move[1]
    if next_row>=1 and next_row <= 8 and next_col >=1 and next_col <= 8:
        result += 1

print (result)