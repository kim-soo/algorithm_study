from copy import deepcopy

n, l = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 만약 높이가 모두 같으면 지나갈수잇음
# 높이 차이가 1일경우 경사로 놓을 수 있음
#     1. 낮은 칸 높이가 모두 같아야함
#     2. L개의 칸이 연속으로 해당 높이여야 함
#     3. 범위를 벗어나면 안됨

def move(test_list, n, l):
    test = 1
    structed = [0] * n
    for i in range(n-1):
        if test_list[i] == test_list[i+1]:
            continue
        elif test_list[i] + 1 == test_list[i+1]:
            for k in range(l):
                if 0 <= i-k < n:
                    if structed[i-k] == 0 and (test_list[i-k] == test_list[i+1] -1 ):    #이미 경사로 지어진지 확인
                        continue
                    else:
                        test = 0
                        break
                else:
                    test = 0
                    break
            if test == 1:
                for k in range(l):
                    structed[i-k] = 1           #경사로 지어진 곳 표시
        elif test_list[i] - 1 == test_list[i+1]:
            for k in range(1, l+1):
                if 0 <= i+k < n:
                    if structed[i + k] ==0 and (test_list[i+k] == test_list[i] -1):   #이미 경사로 지어진지 확인
                        continue
                    else:
                        test = 0
                        break
                else:
                    test = 0
                    break
            if test == 1:
                for k in range(1, l+1):
                    structed[i+k] = 1     #경사로 지어진 곳 표시
        else:
            test = 0
            break
    if test == 1:
        return 1

test_list = []
test_list = deepcopy(graph)
result = 0
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(graph[j][i])
    test_list.append(tmp)

for k in range(len(test_list)):
    if move(test_list[k], n, l) == 1:
        result +=1

print(result)