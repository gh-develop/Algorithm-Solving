import sys
from collections import deque

# sys.stdin = open('bj_9012_stack_in.txt', 'r')
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    command = input().strip()
    stack = deque()
    for ch in command:
        if ch == '(':
            stack.append(ch)
        elif ch == ')' and stack:
            stack.pop()
        else:
            stack.append('x')
            break
    if stack:
        print('NO')
    else:
        print('YES')
    # print(input().strip())
    # print(input())