import sys

sys.stdin = open('bj_14425_in.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().strip().split())
s = set()
ans = 0

for _ in range(n):
    s.add(input().strip())

# print(set)
for _ in range(m):
    if input().strip() in s:
        ans += 1
print(ans)