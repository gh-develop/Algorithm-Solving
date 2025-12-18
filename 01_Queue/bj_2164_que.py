import sys
from collections import deque

# sys.stdin = open("bj_2164_in.txt", 'r')
input = sys.stdin.readline

n = int(input())
que = deque(i for i in range(1, n+1))

while len(que) > 1:
    que.popleft()
    x = que.popleft()
    que.append(x)

print(que[0])