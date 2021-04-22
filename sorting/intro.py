# 정렬 Sorting
# 데이터를 특정한 기준에 따라서 순서대로 나열하는 것
# 정렬 알고리즘은 이진 탐색의 전처리 과정이기도 하니 제대로 알고 넘어가야 한다.
# 상황에 적절한 정렬 알고리즘을 사용해야 효율적이게 동작한다.
# 선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬

# 선택 정렬
# Selection Sort
# 무작위로 데이터가 있을 때, 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 "바꾸고", 그 다음 작은 데이터를 앞에서 두번째 데이터와 바꾸는 과정
# "매번" "가장 작은" 것을 선택한다고 해서 선택 정렬이다.

print("선택 정렬 예제 코드")
array = [5, 7, 2, 1, 6, 8, 3, 4, 9]
for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
# 시간 복잡도는 간단히 O(N^2)


# 삽입 정렬
# Insertion Sort
# 필요할 때만 위치를 바꾼다.
# 데이터가 거의 정렬 되어 있을때 효율 적이다.
# 삽입 정렬은 특정 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있따고 가정한다.
# 정렬되어 있는 데이터 리스트에서 적절한 위치를 찾은 뒤에, 그 위치에 삽입 된다는 점이 특징이다.
# 첫 번째 데이터는 그 자체로 정렬되어 있다고 판단해서, 두번째 데이터를 어디 위치로 둘지부터 정한다.
# 시간 복잡도는 O(N^2)
print("삽입 정렬 예제 코드")
array = [5, 7, 2, 1, 6, 8, 3, 4, 9]
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)


# 퀵 정렬
# 정렬 알고리즘 중에 가장 많이 사용된다!@!
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
# 퀵 정렬은 기준을 설정하고, 큰수와 작은수를 교환한 다음 리스트를 반으로 나누는 방식으로 동작한다.
# 그 교환하기 위한 기준을 pivot "피벗"이라고 한다.
# 피벗을 정한후 그보다 작은 쪽과 큰쪽으로 두가지로 나뉘면
# 왼쪽리스트, 즉 pivot보다 작은 쪽만 개별적으로 정렬시키면
# 그니까 분할된 두개를 다시 pivot을 설정하여 정렬시킨다는 의미임.
# 그러려면 바로 재귀함수를 잘 쓸줄 알아야한다~

print("퀵 정렬 소스코드")
array = [5, 7, 2, 1, 6, 8, 3, 4, 9]


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array)-1)
print(array)

# 계수 정렬
# Count sort
# 특정 조건이 부합할 때만 사용할수 있다.
# 데이터의 크기범위가 제한되어 정수 형태로 표현할 수있을때만 사용가능하다
# 예를들면 1~100의 성적데이터를 정렬한다던지.
# 모든 범위를 담을 수있는 크기의 리스트를 선언해야하기때문에, 가장 작은 데이터와 가장 큰데이터의 차이가 너무 크다면 사용 불가하다


# 선택, 삽입, 퀵 정렬은 데이터를 비교하며 위치를 변경하며 정렬하는 방식
# 계수 정렬은 비교 기반의 정렬 알고리즘이 아님.

# 하지만 대게 그냥 정렬 라이브러리를 쓰기 마련이다.
# 파이썬은 기본적으로 sorted() , sort() 가 존재한다
# listname.sort(), listname.sort(reverse = True)
# sorted(listname) sorted는 새로운 리스트를 반환한다(!!원본리스트에는 영향이 없다!!)
# 그냥 원본을 바꾸면서 속도가 더 빠른것이 sort().
# 원본을 건드리지 않으러면 sorted()
