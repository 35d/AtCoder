# ABC085C - Otoshidama
# https://atcoder.jp/contests/abs/tasks/abc085_c

# スペース区切りの整数の入力
list = list(map(int, input().split()))
N = list[0]
Y = list[1]

answer = '-1 -1 -1'

# 以下のように定義
# A 10,000円札の枚数
# B 5,000円札の枚数
# C 1,000円札の枚数
for A in range(N + 1):
    for B in range(N + 1):
        for C in range(N + 1):
            # print(A, B, C, 10000 * A + 5000 * B + 1000 * C, A + B + C, 10000 * A + 5000 * B + 1000 * C == Y, A + B + C == N)
            if 10000 * A + 5000 * B + 1000 * C == Y and A + B + C == N:
                answer = str(A) + " " + str(B) + " " + str(C)

print(answer)
