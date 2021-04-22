# 프로그래머스 문제
def solution(nums):
    data = set(nums)
    print(data, len(data))
    division = len(nums)//2
    print(division)
    if len(data) < division:
        return len(data)
    else:
        return division


print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
