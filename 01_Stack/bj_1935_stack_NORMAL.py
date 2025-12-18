import sys
from collections import deque

# sys.stdin = open('bj_1935_in.txt', 'r')
open = sys.stdin.readline

stack = deque()
number = []
n = int(input())
command = input().strip()

for _ in range(n):
    number.append(int(input().strip())) # 문자별 숫자 치환값

# print(ord('A'))
for ch in command:
    if 'A' <= ch <= 'Z': #대문자면
        stack.append(number[ord(ch) - ord('A')])
    else: #문자가 아니면
        back_number = stack.pop()
        front_number = stack.pop()
        if ch == '+':
            result = front_number + back_number
        elif ch == '-':
            result = front_number - back_number
        elif ch == '*':
            result = front_number * back_number
        elif ch == '/':
            result = front_number / back_number

        stack.append(result)
print(f"{stack[0]:.2f}")