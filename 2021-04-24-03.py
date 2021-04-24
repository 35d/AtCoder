#
# https://atcoder.jp/contests/abc199/tasks/abc199_c

N = int(input())
S = input()
Q = int(input())

T = [0] * Q
A = [0] * Q
B = [0] * Q

# 自分の回答（実行時間が駄目だった間に合わなかった）
# for i in range(Q):
#     T[i], A[i], B[i] = map(int, input().split())

# l = list(S)

# for i in range(Q):
#     if T[i] == 1:
#         l[A[i] - 1], l[B[i] - 1] = l[B[i] - 1], l[A[i] - 1]
#     else:
#         l = l[N:]+l[0:N]

# print("".join(l))
