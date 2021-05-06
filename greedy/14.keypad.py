# 2020 카카오 인턴쉽 - 키패드 누르기

# 문제 해결 사고 흐름 과정을 그대로 담아 두었기떄문에
# 미래의 내가 보고 배우는게 있길 바라는 마음에 과정 그대로 두기로함


# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #   -> 10 11 12

# start = *(L) , #(R)
# 각 손가락은 상하좌우만 이동가능
# 왼쪽 열 1,4,7 을 입력할 때는 왼손 엄지
# 오른쪽 열 3 6 9 는 오른손 엄지
# 가운데열 4개는 두 엄지중 현재 키패드 위치에서 더 가까운 손가락 사용
# 만약 거리가 같다면 오른손 잡이는 오른손으로, 왼손잡이는 왼손으로

# 중요한건 result는  L,R 이므로,

# def solution(numbers, hand):
#    result = []
#    L = 10
#    R = 12
#    for num in numbers:
#        if num in [1, 4, 7]:
#            result.append("L")
#            L = num
#            print("L: ", L)
#        elif num in [3, 6, 9]:
#            result.append("R")
#            R = num
#            print("R: ", R)
#        # 나머지 2, 5, 8, 0 일때
#        elif num in [2, 5, 8, 0]:
#            gap_L = abs(L - (num - 1))
#            gap_R = abs(R - (num + 1))
#            if gap_L < gap_R:
#                result.append("L")
#                L = num
#                print("L: ", L)
#            elif gap_R < gap_L:
#                result.append("R")
#                R = num
#                print("R: ", R)
#            elif gap_L == gap_R:
#                result.append(hand)

# 일단 세로길이는 행간의 차이로, 나머지는 절댓값 차로해서 더 작은수인 걸로 하자
# 만약, L=1, R=6 일때  2를 눌러야 한다
# 1의 행 인덱스 0,  2의 행 인덱스 0, 6의 행 인덱스 1
# 이때 abs(0-0) < abs(0 - 1) 이므로 L로 누르게 된다

# 2, 5, 8, 0 일때
# 왼쪽기준 -1 오른쪽 기준 +1 한다음 ,현재 L , R 위치에서 뺀 값으로 매기자
# 만약 순서대로 갈때 현재 , L = 4 R = 3  일때 5를 눌러야하는데
# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #   -> 10 11 12
# gap_L = abs(L - (num - 1))   => 4 - 4 = 0
# gap_R = abs(R - (num + 1))   => abs(3 - 6) = 3
# gap_L 이 더작으므로 L로 누른다.

# L = 4 , R = 2 일때 5같은거 누를려고하면
# 둘다 거리가 1인데 현재 내 알고리즘으론 그렇지 못하다.

# 만약 거리가 같다면 오른손이면 오른손 왼손이면 왼손
# for문 돌때마다 현재 손이 어디에 있는지 기록해두어야함.

# def solution(numbers, hand):
#    result = []
#    if hand == "right":
#        hand = "R"
#    elif hand == "left":
#        hand = "L"

#    pads = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
#    # [행열의 위치, 행의 위치(거리계산용), 열의 위치]
#    L = [pads[3][0], 3, 0]
#    R = [pads[3][2], 3, 0]
#    for num in numbers:
#        print("result: ", result)
#        for i in range(0, len(pads)):  # i 는 행 (현재 4행)
#            # for j in range(0, len(pads[i])):  # j는 열 (현재 3열)
#            # 무조건 왼
#            if num == pads[i][0]:
#                result.append(["L", num])
#                L = [pads[i][0], i, 0]
#                print("num: ", num)
#                print(L)

# 무조건 오
#            elif num == pads[i][2]:
#                result.append(["R", num])
#                R = [pads[i][2], i, 2]
#                print("num: ", num)
#                print(R)

# 2 5 8 0
#            elif num == pads[i][1]:
# (행-행) + (열-열)
#                gap_L = abs((L[1] - i)) + abs((L[2] - 1))
#               gap_R = abs((R[1] - i)) + abs((R[2] - 1))
#                print("num: ", num, "gap_L: ", gap_L, "gap_R: ", gap_R)
#                if gap_L < gap_R:
#                    result.append(["L", num])
#                    L = [pads[i][1], i, 1]

#                    print("num: ", num)
#                    print(L)
#                elif gap_R < gap_L:
#                    result.append(["R", num])
#                    R = [pads[i][1], i, 1]
#                    print("num: ", num)
#                    print(R)
#                elif gap_R == gap_L:
#                    result.append([hand, num])
#                    if hand == "L":
#                        L = [pads[i][1], i, 1]
#                        print("num: ", num)
#                        print(L)
#                    elif hand == "R":
#                        R = [pads[i][1], i, 1]
#                        print("num: ", num)
#                        print(R)
#    return result

# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #   -> 10 11 12

# 만약 5를 눌러야 하는데, L=4 , R=3 이다
# 4 = (2행 1열), 3 = (1행 3열), 5 = (2행 2열)
# 4 와 5의 거리는 (2-2 + 2 - 1) = 1 , abs해줄것
# 3 와 5의 거리는 (2-1 + 2 - 3) = 2
# 만약 5를 눌러야 하는데, L=1, R= 12 이다
# 1 = (1행1열), 12 = (4행 3열), 5 = (2행 2열)
# 1과 5의 거리는 2, 5와 12의 거리는 3
# 아 됬다. 각 (행-행) + (열-열) 비교


#print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))


# 1 : L
# 3 : R
# 4 : L
# 5 : L
# 8 : L
# 2 : R
# 1 : L
# 4 : L
# 5 : R
# 9 : R
# 5 : L

def solution(numbers, hand):
    result = []
    if hand == "right":
        hand = "R"
    elif hand == "left":
        hand = "L"

    pads = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 0, 12]]
    # [행열의 위치, 행의 위치(거리계산용), 열의 위치]
    L = [pads[3][0], 3, 0]
    R = [pads[3][2], 3, 0]
    for num in numbers:
        for i in range(0, len(pads)):  # i 는 행 (현재 4행)
            # for j in range(0, len(pads[i])):  # j는 열 (현재 3열)
            # 무조건 왼
            if num == pads[i][0]:
                result.append("L")
                L = [pads[i][0], i, 0]

            # 무조건 오
            elif num == pads[i][2]:
                result.append("R")
                R = [pads[i][2], i, 2]

            # 2 5 8 0
            elif num == pads[i][1]:
                # (행-행) + (열-열)
                gap_L = abs((L[1] - i)) + abs((L[2] - 1))
                gap_R = abs((R[1] - i)) + abs((R[2] - 1))
                if gap_L < gap_R:
                    result.append("L")
                    L = [pads[i][1], i, 1]

                elif gap_R < gap_L:
                    result.append("R")
                    R = [pads[i][1], i, 1]

                elif gap_R == gap_L:
                    result.append(hand)
                    if hand == "L":
                        L = [pads[i][1], i, 1]

                    elif hand == "R":
                        R = [pads[i][1], i, 1]

    return ''.join(result)


#print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
