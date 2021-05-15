# 떡볶이 떡 만들기

# 예제
# 19, 14, 10, 17 의 떡들이 나란히 있고 절단기 높이를 15
# 15, 14, 10, 15 가 된다
# 잘린떡은
# 4, 0, 0, 2 이고 손님은 총 6을 가져간다.
# 손님이 요청한 총 길이가 M 일떄 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하자


# 전형적인 이진탐색 문제
# Parametric Search 유형의 문제이다.(최적화 문제를 결정 문제로 (예 or 아니오)로 바꾸어 해결하는 기법)
# 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제
# 적절한 높이를 찾을 때까지 절단기의 높이 H를 반복해서 조정하자

n, m = list(map(int, input().split()))

array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
