# 이진 탐색
# Binary Search
# 리스트 내에서 데이터를 매우 빠르게 탐색하는 이진 탐색 알고리즘
# 기본적을 순차탐색은 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법이다
# 주로 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용한다.

# 이진 탐색 : 반으로 쪼개면서 탐색하기
# 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.
# 데이터가 무작위일 때는 사용할 수 없다.
# 탐색범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있다.
# 이진 탐색은 변수를 3개 사용한다
# 시작점, 끝점, 중간점.
# 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 것이다.
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재 하지 않습니다.")
else:
    print(result + 1)


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] = target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재 하지 않습니다")
else:
    print(result + 1)
