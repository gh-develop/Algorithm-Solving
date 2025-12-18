import sys
from collections import deque

sys.stdin = open("bj_1158_que_in.txt", 'r')
# input = sys.stdin.readline


n, k = map(int, input().strip().split())
que = deque([i for i in range(1, n+1)])
ans = []
while que:
    que.rotate(-(k-1))
    ans.append(que.popleft())

print(f"<{', '.join(map(str, ans))}>")
