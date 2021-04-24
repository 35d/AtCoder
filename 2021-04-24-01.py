#
# https://atcoder.jp/contests/abc199/tasks/abc199_a

# スペース区切りの整数の入力
list = list(map(int, input().split()))
A = list[0]
B = list[1]
C = list[2]

answer = 'No'

if A * A + B * B < C * C:
    answer = 'Yes'


print(answer)
