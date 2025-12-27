import sys
from collections import deque
from itertools import combinations

# sys.stdin = open('bj_2800_in.txt', 'r')
input = sys.stdin.readline

command = list(input().strip())
command_length = len(command)
# print(command)

stack = []
brackets = []
ans = set()

for i in range(command_length):
    if command[i] == '(':  # 열린 괄호면
        stack.append((i, command[i]))
    elif stack and command[i] == ')':  # 닫힌 괄호면
        start = stack.pop()
        brackets.append((start[0], i))
# print(bracket)
for i in range(1, len(brackets) + 1):  # 괄호 조합 1~ 괄호 개수
    comb = list(combinations(brackets, i))
    # print(comb)
    for ch in comb:  # 괄호 조합
        s = set()
        for j in range(i):  # 괄호 시작, 끝 인덱스를 set에 추가
            s.add(ch[j][0])
            s.add(ch[j][1])
            # print(ch[j])

        # print(s)
        arr = []
        for k in range(command_length):
            if k in s:  # 주어진 문자식의 인덱스가 괄호조합의 인덱스면
                continue
            else:
                arr.append(command[k])
        # print(arr)
        tmp = ''.join(arr)
        # print(tmp)
        ans.add(tmp)  # 중복제거를 위해 set 사용

        # print(ch)

result = sorted(ans)
for line in result:
    print(line)
