# 프로그래머스 데브매칭 2021   로또의 최고 순위와 최저 순위


# 일단은 0인 걸 따로 세어놓고
# 그리고 민우꺼랑 당첨번호 일치하는걸 따로 기록해두고
# 0을 포함전부시킨것의 순위, 안포함시킨것의 순위로
# 등수를 매깁니다.
def grade(n):
    if n == 6:
        return 1
    elif n == 5:
        return 2
    elif n == 4:
        return 3
    elif n == 3:
        return 4
    elif n == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    # 0의 갯수
    count_zero = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            count_zero += 1
    print("0의 갯수 : ", count_zero)
    # 입력받은 두 리스트안에서 겹치는 번호 갯수
    equal_num = []
    for num in lottos:
        for win in win_nums:
            if num == win:
                equal_num.append(num)
    print("동일한 숫자 갯수: ", equal_num)

    max_grade = count_zero + len(equal_num)
    min_grade = len(equal_num)
    print(max_grade, min_grade)
    return [grade(max_grade), grade(min_grade)]


# print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
# 앞의 리스트가 민우꺼
