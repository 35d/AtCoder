# ABC083B - Some Sums
# https://atcoder.jp/contests/abs/tasks/abc083_b

# スペース区切りの整数入力
l = list(map(int, input().split()))
N = l[0]
A = l[1]
B = l[2]

answer = 0

for n in range(0, N + 1):
    # n を桁ごとに分割して配列化
    l = [int(x) for x in list(str(n))]

    # 各桁の合計値を計算
    sumA = 0
    for digit in l:
        sumA += digit
    if sumA >= A and sumA <= B:
        answer += n


print(answer)
