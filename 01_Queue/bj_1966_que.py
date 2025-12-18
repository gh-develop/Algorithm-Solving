import sys
from collections import deque
import math

# sys.stdin = open('bj_1966_in.txt', 'r')
open = sys.stdin.readline

tc= int(input())

for _ in range(tc):
    n, m = map(int, input().strip().split())
    priority = deque([i for i in map(int, input().strip().split())])
    max_priority = max(priority)
    # print(max_priority)
    cnt = 0
    while priority:
        if priority[0] >= max_priority: # 출력 될 때
            cnt += 1 # 나간 순서
            if m == 0: # 대상이 출력일 때
                break
            else: # 다른게 출력 되면
                priority.popleft() #출력
                m -= 1 # 인덱스 재계산
                max_priority = max(priority) # 최대우선 순위 재계산
        else: # 출력 안될 때
            priority.append(priority.popleft()) # 맨 뒤로 보냄
            if m > 0:
                m -= 1
            else:
                m = len(priority) -1

    print(cnt)


