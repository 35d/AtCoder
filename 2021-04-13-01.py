# ABC088B - Card Game for Two
# https://atcoder.jp/contests/abs/tasks/abc088_b

# 整数の入力
N = int(input())

# スペース区切りの整数の入力
list = list(map(int, input().split()))

alice = 0
bob = 0
isAliceTurn = True

while len(list) > 0:
    max_num = max(list)  # list の中の最大値
    index = list.index(max_num)  # list の中の最大値インデックス
    if isAliceTurn:
        alice += max_num
    else:
        bob += max_num
    list.pop(index)
    isAliceTurn = not isAliceTurn

print(alice - bob)
