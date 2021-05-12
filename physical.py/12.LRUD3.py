# 프로그래머스
# 방문 길이


# def solution(dirs):
#    x = 0
#    y = 0
#    result = []

# (x, y) = (렬, 행)
#    direction = ["L", "R", "U", "D"]
#    dx = [-1, 1, 0, 0]
#    dy = [0, 0, 1, -1]
#    for dir in dirs:
#        for i in range(len(direction)):
#            if dir == direction[i]:
#                nx = x + dx[i]
#                ny = y + dy[i]
#                #result += 1
#        if nx > 5 or nx < -5 or ny > 5 or ny < -5:
#            #result -= 1
#           continue
#
#       x, y = nx, ny
#        result.append(str(nx)+str(ny))
#   new_result = result[1:len(result)]
# rint("result :", result)
# print("new_result :", new_result, nx, ny)
# print(set(new_result))
#   return len(set(new_result)) + 1

# if dir == "L":
#    x = x + dx[0]
#    y = y + dy[0]
#    result += 1
# elif dir == "R":
#    x = x + dx[1]
#    y = y + dy[1]
#    result += 1
# elif dir == "U":
#    x = x + dx[2]
#    y = y + dy[2]
#    result += 1
# elif dir == "D":
#    x = x + dx[3]
#    y = y + dy[3]
#    result += 1
# if x > 5 or y > 5 or x < -5 or y < -5:
#    continue
# print(dir, x, y)
# return result - 2
def solution(dirs):
    result = 0
    visited = set()
    x, y = 0, 0

    direction = ["L", "R", "U", "D"]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for dir in dirs:
        for i in range(len(direction)):
            if dir == direction[i]:
                nx = x + dx[i]
                ny = y + dy[i]
                if nx > 5 or nx < -5 or ny > 5 or ny < -5:
                    continue
                if (x, y, nx, ny) not in visited:
                    visited.add((x, y, nx, ny))
                    visited.add((nx, ny, x, y))
                    result += 1
                    print(visited)
                x, y = nx, ny
                # print(visited)
                print(result)


print(solution("ULURRDLLU"))
# print(solution("LULLLLLLU"))


# 길이 (0,1)->(-1,1) 에서 간거랑 (-1,1)->(0,1)은 같은길로 치니까 이 점 유의 해야함.
# set 자료형은 순서가 없기(unordered) 때문에 인덱싱으로 값을 얻을 수 없다. 어떤 값이 먼저 나올지 알 수 없다.
