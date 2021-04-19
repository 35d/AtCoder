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

# パフォーマンスが厳しい
# for A in range(N + 1):
#     # 1,0000円札で総額を超えたらもう組み合わせはほかにないので break する
#     if 10000 * A > Y:
#         break
#     for B in reversed(range(N + 1 - A)):
#         C = N - A - B
#         print(A, B, C, 10000 * A + 5000 * B + 1000 * C, A + B + C,
#               10000 * A + 5000 * B + 1000 * C == Y, A + B + C == N)
#         if 10000 * A + 5000 * B + 1000 * C == Y:
#             answer = str(A) + " " + str(B) + " " + str(C)
#             break

for A in reversed(range(N + 1)):
    if A * 10000 > Y:
        continue
    if answer != '-1 -1 -1':  # 答えが1つでも見つかったらもう計算不要なのでループを抜ける
        break
    for B in reversed(range(N + 1 - A)):
        if A * 10000 + B * 5000 > Y:
            continue
        C = N - A - B
        sum = 10000 * A + 5000 * B + 1000 * C
        # print(A, B, C, sum, sum == Y)
        if sum == Y:
            answer = str(A) + " " + str(B) + " " + str(C)
            break

print(answer)
