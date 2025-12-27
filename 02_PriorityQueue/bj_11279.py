import sys
import heapq

sys.stdin = open('bj_11279_in.txt', 'r')
input = sys.stdin.readline

n = int(input().strip())
pq = []
for _ in range(n):
    command = int(input().strip())
    if not pq and command == 0:
        print(0)
    elif pq and command == 0:
        print(-heapq.heappop(pq))
    else:
        heapq.heappush(pq, -command)
