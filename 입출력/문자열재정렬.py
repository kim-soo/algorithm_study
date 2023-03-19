S = input()

string= []
num = 0

for i in S:
    if i.isalpha():
        string.append(i)
    else :
        num += int(i)

string.sort()
if num != 0:
    string.append(str(num))
result = ''.join(string)

print(result)
