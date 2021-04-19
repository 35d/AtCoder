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
    print(D)
    print(len(D))
    max_num = max(D)  # 直径の最大値を代入

    # 数値が D 以上のものをすべて pop する
    for i in range(len(D)):
        print(i)
        print('D[i]:', D[i])
        if D[i] >= max_num:
            D.pop(i)

    count += count

print(count)
