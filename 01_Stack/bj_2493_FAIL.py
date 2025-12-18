import sys

sys.stdin = open("bj_2493_in.txt", 'r')
input = sys.stdin.readline
write = sys.stdout.write

n = int(input().strip())
high_top_list = [(999999999, 0)] # 높은 탑들의 값과 위치 저장
top_list = [0]+list(map(int, input().strip().split()))
ans = []

for i in range(1, n+1):
    if top_list[i] <= high_top_list[-1][0]: # 하이탑이 더 크거나 같다면
        # ans.append(high_top_list[-1][1])
        write(str(high_top_list[-1][1]) + ' ')
        high_top_list.append((top_list[i], i))
    else: #하이탑이 더 작다면 더 큰 하이탑이 나올때까지 pop한 후에 append
        while top_list[i] > high_top_list[-1][0]:
            high_top_list.pop()

        # ans.append(high_top_list[-1][1])
        write(str(high_top_list[-1][1]) + ' ')
        high_top_list.append((top_list[i], i))


# sys.stdout.write(' '.join(map(str, ans)))





