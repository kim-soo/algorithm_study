# 순열이란 서로 다른 n개 중에 r개를 선택하는 경우, 순서 상관 있음 nPr
# 조합이란 서로다른 n개 중에 r개를 선택하는 경우, 순서 상관 없음 nCr


def permutation (arr, r):
    arr = sorted (arr)
    used = [0 for _ in range(len(arr))]
    
    def generate(chosen, used):
        if len(chosen) == r:
            print(chosen)
            return
    
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i]=0
                chosen.pop()

    generate([], used)