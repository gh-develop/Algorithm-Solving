import sys
from collections import deque

sys.stdin = open('bj_22942_in.txt', 'r')
input = sys.stdin.readline

n = int(input().strip())
dq = deque()

for _ in range(n):
    x, r = map(int, input().strip().split())

    # 체크 덱
    if dq:
        top = dq[-1]
        # 원의 위치 상태 체크
        top_x = top[0][0]
        top_r = top[0][1]
        if abs(top_x - x) > top_r + r: # 외부의 원
            dq.append((x, r))
        elif abs(top_x - x) < abs(top_r - r) or (top_x == x and top_r != r): #내부의 원

    else:
        dq.append((x, r))
