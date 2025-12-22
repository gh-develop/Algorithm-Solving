import sys
sys.stdin = open('bj_22942_in.txt', 'r')
input = sys.stdin.readline

n = int(input().strip())
circle = []

for _ in range(n):
    x, r = map(int, input().strip().split())
    circle.append((x-r, x+r))

circle.sort(key = lambda x: (x[0], x[1])) # 원의 시작점 오름차순, 원의 끝점 오름차순, nlog(n)
# 제일 왼쪽부터 시작하는 원, 스택의 하단으로 갈수록 원을 포함하는 바깥 원으로 이동
stack = []
for c in circle:
    if stack:
        while stack:
            if stack[-1][1] < c[0]:
                stack.pop()
            else:
                break

        if stack:
            if stack[-1][0] < c[0] and c[1] < stack[-1][1]:
                stack.append(c)
            else:
                print('NO')
                exit(0)
        else:
            stack.append(c)
    else:
        stack.append(c)

print('YES')





















# N = int(input())
# circles = []
#
# for _ in range(N):
#     x, r = map(int, input().split()) #입력 받기
#     circles.append((x - r, x + r))  # (begin, end) #원의 양 끝점 저장
#
# # begin 오름차순, begin 같으면 end 오름차순
# circles.sort(key=lambda x: (x[0], x[1]))
#
# is_valid = True
# end_stack = []
#
# for begin, end in circles:
#     # 이미 끝난 원들 제거
#     while end_stack and end_stack[-1] < begin:
#         end_stack.pop()
#
#     # 다른 원 내부에 시작해서 끝이 걸치는 경우 → 교차
#     if end_stack and begin <= end_stack[-1] <= end:
#         is_valid = False
#         break
#
#     end_stack.append(end)
#
# print("YES" if is_valid else "NO")
