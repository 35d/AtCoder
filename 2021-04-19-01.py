# ABC085B - Kagami Mochi
# https://atcoder.jp/contests/abs/tasks/abc085_b

# 整数の入力
N = int(input())
D = []  # 餅のリスト

# リストAにappend()を使って格納していく
for _ in range(N):
    D.append(input())

flg = True
count = 0

while len(D) > 0:
    max_num = max(D)  # 直径の最大値を代入

    while D.count(max_num) != 0:
        index = D.index(max_num)
        D.pop(index)

    count = count + 1

print(count)
