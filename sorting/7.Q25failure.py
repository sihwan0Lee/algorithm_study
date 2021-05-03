# 실패율
# 2019 카카오 신입 공채 1차

# 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무크다
# 실패율의 정의
# 스페이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

# 전체 스테이지의 개수 N
# 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때
# 실패율이 높은 스테이지 부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 반환하시오

# stages = [2, 1, 2, 6, 2, 4, 3, 3] ,  N = 5
# 실패율은 순서대로
# 스테이지 1에 남은건 1명뿐 -> 실패율 1/8
# 스테이지 2에 남은건 3명 -> 3/7

# 일단 sort() 해줘야되고, -> [1, 2, 2, 2, 3, 3, 4, 6]
# 카운트로 올려서 걍 나눠주고 , 그거 다시 리스트에 담아서 정리하면 될듯.

def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        print(answer)
        length -= count

    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    print(answer)

    answer = [i[0] for i in answer]
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
