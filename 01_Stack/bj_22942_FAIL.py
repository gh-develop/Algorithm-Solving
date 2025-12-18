import sys
input = sys.stdin.readline

N = int(input())
circles = []

for _ in range(N):
    x, r = map(int, input().split())
    circles.append((x - r, x + r))  # (begin, end)

# begin 오름차순, begin 같으면 end 오름차순
circles.sort(key=lambda x: (x[0], x[1]))

is_valid = True
end_stack = []

for begin, end in circles:
    # 이미 끝난 원들 제거
    while end_stack and end_stack[-1] < begin:
        end_stack.pop()

    # 다른 원 내부에 시작해서 끝이 걸치는 경우 → 교차
    if end_stack and begin <= end_stack[-1] <= end:
        is_valid = False
        break

    end_stack.append(end)

print("YES" if is_valid else "NO")
