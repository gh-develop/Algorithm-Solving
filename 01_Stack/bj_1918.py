import sys

# sys.stdin = open('bj_1918_in.txt', 'r')
input = sys.stdin.readline
rs = []
stack = []

cal_p = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}  # 우선순위 값

for ch in input().strip():
    if ch.isalpha():  # 알파벳
        rs.append(ch)
    elif ch == '(':  # 열린괄호
        stack.append(ch)
    elif ch == ')':  # 닫힌괄호
        while stack and stack[-1] != '(':
            rs.append(stack.pop())
        stack.pop()  # '(' 제거
    else:  # 연산자들
        while stack and cal_p[stack[-1]] >= cal_p[ch]:
            rs.append(stack.pop())
        stack.append(ch)
while stack:
    rs.append(stack.pop())

print(''.join(rs))
