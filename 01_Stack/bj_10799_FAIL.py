import sys

sys.stdin = open('bj_10799_in.txt', 'r')
input = sys.stdin.readline
# s = sys.stdin.read().strip()
s = input().strip()

total = 0
pipe_stack = 0
is_opened = True

for ch in s:
    if ch == '(':
        # start of pipe
        pipe_stack += 1
        is_opened = True
    elif ch == ')' and is_opened:
        # laser 레이저를 만나면 현재까지 오픈된 파이프를 잘라서 갯수 생성(확정된 파이프 개수)
        pipe_stack -= 1
        total += pipe_stack
        is_opened = False
    else:  # ch == ')' and not is_opened
        # end of pipe 파이프가 끝나면 레이저 뒷부분 1조각이 남으므로 그거 추가
        pipe_stack -= 1
        total += 1
        is_opened = False
    print(total)
# print(total)