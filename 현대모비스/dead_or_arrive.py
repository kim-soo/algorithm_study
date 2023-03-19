# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque
import sys
num = int(input())
v= [0] * (num)
w = [0] * (num)
rslt = deque()

for i in range(num):
	v[i], w[i] = map(int, sys.stdin.readline().split())
	
for i in range(num):
    rslt.append(i)
    for j in range(0, i):
        if v[j] == v[i] and j in rslt:
            if w[i] < w[j]:
                rslt.remove(i)
            else:
                rslt.remove(j)

print(sum(rslt) + len(rslt))
