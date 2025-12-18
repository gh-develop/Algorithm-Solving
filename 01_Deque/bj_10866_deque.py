import sys
from collections import deque

# sys.stdin = open("bj_10866_in.txt", 'r')
input = sys.stdin.readline

dq = deque()

n = int(input())
for _ in range(n):
    command = input().strip().split()

    if command[0] == 'push_front':
        dq.appendleft(command[1])
    if command[0] == 'push_back':
        dq.append(command[1])
    if command[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    if command[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    if command[0] == 'size':
        print(len(dq))
    if command[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    if command[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    if command[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)




