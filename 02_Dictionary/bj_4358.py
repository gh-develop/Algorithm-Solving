import sys

sys.stdin = open('bj_4358_in.txt', 'r')
input = sys.stdin.readline

tree_count = {}
tot_cnt = 0

while True:
    tree = input().strip()
    # print(tree)
    if not tree:
        break
    tot_cnt += 1
    # print(dict.get(tree))
    tree_count[tree] = tree_count.get(tree, 0) + 1

# sorted_dict = sorted(tree_count.items())
# print(sorted_dict)
for tree in sorted(tree_count):
    ratio = (tree_count[tree] / tot_cnt) * 100
    print(f"{tree} {ratio:.4f}")

'''
반올림 계산시 round 금지, format으로 해결할 것
'''