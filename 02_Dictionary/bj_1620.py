import sys

sys.stdin = open('bj_1620_in.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().strip().split())
name_dict = {}
index_dict = {}

for i in range(1, n+1):
    name = input().strip()
    name_dict[name] = i
    index_dict[str(i)] = name

# print(name_dict, index_dict)
for _ in range(m):
    command = input().strip()
    if command.isalpha():
        print(name_dict[command])
    else:
        print(index_dict[command])