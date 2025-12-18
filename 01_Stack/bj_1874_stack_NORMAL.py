# import sys
#
# sys.stdin = open('bj_1874_in.txt', 'r')
# # open = sys.stdin.readline
#
# n = int(input())
#
# stack = []
# num = 1
# answer = []
#
# for i in range(n):
#     su = int(input())
#
#     while su >= num:
#         stack.append(num)
#         num += 1
#         answer.append('+')
#         answer.append('\n')
#
#     if stack and stack[-1] == su:
#         answer.append("-")
#         answer.append('\n')
#         stack.pop()
#
#     else:
#         answer = ['N', 'O', '\n']
#         break
#
# sys.stdout.write(''.join(answer))


import sys

input = sys.stdin.readline

N = int(input())

remain = 1
stack = []
answer = []   # 출력 버퍼 (문자 단위)

for _ in range(N):
    current = int(input())

    while remain <= current:
        stack.append(remain)
        remain += 1
        answer.append('+')
        answer.append('\n')

    if stack and stack[-1] == current:
        stack.pop()
        answer.append('-')
        answer.append('\n')
    else:
        # answer = ['NO']
        answer = ['N', 'O', '\n']
        break

# for i in answer:
#     print(i)
sys.stdout.write(''.join(answer))
