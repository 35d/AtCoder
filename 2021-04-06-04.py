# Welcome to AtCoder
# https://atcoder.jp/contests/abs/tasks/practice_1

# リスト内のすべての要素が偶数かどうかを返す


def isAllEven(list):
    isAllEven = True
    for item in list:
        if item % 2 == 0:
            continue
        else:
            isAllEven = False
    return isAllEven


# 整数の入力
N = int(input())

# スペース区切りの整数の入力
i = map(int, input().split())
list = list(i)

count = 0

while isAllEven(list):
    count = count + 1
    for i in range(len(list)):
        list[i] = int(list[i] / 2)

print(count)
