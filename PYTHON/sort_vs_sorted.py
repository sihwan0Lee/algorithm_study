# 원본을 유지한채, 정렬된 리스트 구하기 - sorted

# 파이썬의 sort() 함수를 사용하면 리스트의 원소를 정렬할 수 있습니다. 
# 이때, sort 함수는 원본의 멤버 순서를 변경합니다.
# 따라서 원본의 순서는 변경하지 않고, 정렬된 값을 구하려면 sort 함수를 사용할 수 없습니다.

# 일반적으로는 deep copy.deepcopy 또는 sort 함수를 씁니다.
list1 = [3, 2, 5, 1]
list2 = [i for i in list1] # 또는 copy.deepcopy를 사용
list2.sort()

# 파이썬에서는 sorted() 가 있습니다
# sorted 함수는 파이썬 내장 함수입니다.
# 첫 번째 매개변수로 들어온 이터러블한 데이터를 새로운 정렬된 리스트로 만들어서 반환해 주는 함수입니다.

list1 = [3, 2, 5, 1]
list2 = sorted(list1)