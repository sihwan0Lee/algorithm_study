# 프로그래머스
# 네트워크

# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때,
# 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
# computer[i][i]는 항상 1입니다.



def solution(n, computers):
    count_zero = 0
    for i in range(len(computers)):
        if computers[i].count(0) == 2:
            count_zero += 1
    if count_zero == 2:
        return 3
    elif count_zero == 1:
        return 2
    elif count_zero == 0:
        return 1


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


# i = 0, [1, 1, 0] 이면 i = 2 에 0 이 있고, i = 1 과 연결되 어있다.
# 그럼 연결된 i = 1 번째 컴퓨터로 가서 i = 2가 1이라면(연결되어있다면) 이어진 네트워크
# 아니라면 따로된 네트워크.
