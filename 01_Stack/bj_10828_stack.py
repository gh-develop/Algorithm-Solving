import sys
from collections import deque

# sys.stdin = open("bj_10828_stack_in.txt", 'r')
# input = sys.stdin.readline
def input():
    return sys.stdin.readline().rstrip()

stack = deque()
N = int(input())
for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    # print(input().strip().split())

