import sys
import heapq
sys.stdin = open('bj_2075_in.txt', 'r')
input = sys.stdin.readline

heap = []

n = int(input().strip())
heap = list(map(int, input().strip().split()))

for _ in range(n-1):
    temp = list(map(int, input().strip().split()))
    for e in temp:
        if heap[0] < e:
            heapq.heappop(heap)
            heapq.heappush(heap, e)

print(heap[0])