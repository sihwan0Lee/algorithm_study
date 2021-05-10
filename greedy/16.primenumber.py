# 소수란 1과 자기자신으로만 나눠떨어지는 수

# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 한다.

from itertools import combinations
# 일단 소수의 정의를 함수로 만들어보자


def prime_number(n):
    prime_count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            prime_count += 1
    if prime_count == 2:
        return True

# 리스트중 임의 3개의수 합의 모든 경우의수 구하는 함수


# def sum_list(nums):
#    sum_list = []
#    sum = 0
#    for i in range(len(nums)):
#        for j in range(1, len(nums)):
#            for k in range(2, len(nums)):
#                if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
#                    sum += (nums[i] + nums[j] + nums[k])
#                    sum_list.append(sum)
#                    sum = 0
#    return set(sum_list)
def sum_list(nums):
    sum_list = []
    result = list(combinations(nums, 3))
    for i in result:
        sum_list.append(sum(i))
    return sum_list


def solution(nums):
    count = 0
    for i in sum_list(nums):
        if prime_number(i) is True:
            count += 1
    return count


print(solution([1, 2, 7, 6, 4]))
# print(prime_number(9))
#print(sum_list([1, 2, 7, 6, 4]))


# sum_list 함수에서 for문을 3번이나 돌려버렸더니 테스트에서 메모리를 너무 잡아먹어서
# 파이썬 내부 모듈을 사용해서 풀었다.
