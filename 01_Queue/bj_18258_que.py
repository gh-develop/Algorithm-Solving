import sys
from collections import deque

# sys.stdin = open("bj_18258_que_in.txt", 'r')
input = sys.stdin.readline

q = deque()
order_n = int(input())
for _ in range(order_n):
    order = list(input().rstrip().split())
    if len(order) >= 2:
        q.append(order[1])
    else:
        if order[0] == 'front':
            if len(q) <= 0:
                print(-1)
            else:
                print(q[0])
        elif order[0] =='back':
            if len(q) <= 0:
                print(-1)
            else:
                print(q[-1])
        elif order[0] == 'size':
            print(len(q))
        elif order[0] == 'empty':
            if len(q) <= 0:
                print(1)
            else:
                print(0)
        elif order[0] == 'pop':
            if len(q) <= 0:
                print(-1)
            else:
                print(q.popleft())

