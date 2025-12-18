import sys
from collections import deque

# sys.stdin = open("bj_2346_in.txt", 'r')
input = sys.stdin.readline

n = int(input())
command = list(map(int,input().strip().split()))

dq = deque((idx, command[idx-1])  for idx in range(1, n+1))
ans = []
while dq:
    # print(dq)
    idx, rotate = dq.popleft()
    ans.append(idx)
    if rotate > 0: # 1칸 덜 간다
        dq.rotate(-(rotate-1))
    else: # 그대로
        dq.rotate(-rotate)

print(*ans)
