# 얻을 수 있는 식량의 최대 값 구하기
# 최소한 한 칸 이상 떨어진 식량창고를 약탈해야만 한다.
n = int(input())

array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])
print(d)

# i = 2
# d[2] = max(d[1], d[0] + array[2]) -> d[2] = 3
# d[3] = max(d[2], d[1] + array[3]) -> d[3] = 8
