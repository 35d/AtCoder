# ABC086A - Product
# https://atcoder.jp/contests/abs/tasks/abc086_a

# スペース区切りの整数の入力
a, b = map(int, input().split())

s = "Even" if (a * b) % 2 == 0 else "Odd"

# 出力
print(s)
