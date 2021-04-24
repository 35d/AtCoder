#
# https://atcoder.jp/contests/abc199/tasks/abc199_b

# 整数の入力
N = int(input())
# スペーズ区切りの整数の入力
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = min(B) - max(A) + 1

if answer > 0:
    print(answer)
    exit()

print(0)
