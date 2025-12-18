import sys
# from collections import deque

sys.stdin = open('bj_2504_in.txt', 'r')
input = sys.stdin.readline


command =  input().strip()
# print(command)
ans = 0
stack = []
flag = True


# 괄호 체크
for ch in command:
    if ch == '(':
        stack.append(ch)
    elif ch == '[':
        stack.append(ch)
    elif ch == ')':  # 닫는 괄호
        if not stack or (stack and stack[-1] != '('):
            print(0)
            exit(0)
        else:
            stack.pop()
    elif ch == ']':  # 닫는 괄호
        if not stack or (stack and stack[-1] != '['):
            print(0)
            exit(0)
        else:
            stack.pop()

if stack:
    print(0)
    exit(0)

stack = []
for ch in command:
    if flag:
        if ch == '(':
            stack.append(ch)
        elif ch == '[':
            stack.append(ch)
        elif ch == ')': # 닫는 괄호
            num = 0
            while 1:
                if stack[-1] == '[': #괄호가 안 맞으면
                    ans = 0
                    flag = False
                    break
                elif num == 0 and stack[-1] == '(':
                    stack.pop()
                    stack.append(2)
                    break
                elif num > 0 and stack[-1] == '(':
                    stack.pop()
                    stack.append(2*num)
                    break
                else: #숫자면 숫자끼리는 덧셈
                    num = num + stack.pop()
        elif ch == ']': # 닫는 괄호
            num = 0
            while 1:
                if stack[-1] == '(':  # 괄호가 안 맞으면
                    ans = 0
                    flag = False
                    break
                elif num == 0 and stack[-1] == '[':
                    stack.pop()
                    stack.append(3)
                    break
                elif num > 0 and stack[-1] == '[':
                    stack.pop()
                    stack.append(3 * num)
                    break
                else:  # 숫자면 숫자끼리는 덧셈
                    num = num + stack.pop()
        # print(stack)
    else:
        break
if flag: ans = sum(stack)
print(ans)