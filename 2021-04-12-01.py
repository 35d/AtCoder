# ABC087B - Coins
# https://atcoder.jp/contests/abs/tasks/abc087_b


# 整数の入力
A = int(input())  # 500円硬貨の枚数
B = int(input())  # 100円硬貨の枚数
C = int(input())  # 50円硬貨の枚数
X = int(input())  # 50の倍数

count = 0  # 場合の数

for a in range(0, A + 1):
    for b in range(0, B + 1):
        for c in range(0, C + 1):
            if a * 500 + b * 100 + c * 50 == X:
                count += 1

print(count)
