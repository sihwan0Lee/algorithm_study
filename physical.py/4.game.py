# N x M크기의 직사각형 게임판
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽방향으로 90도 돌고 안간 칸이있으면 왼쪽으로 한칸
# 안그러면 1번으로 다시 돌아가기
# 4방향 모두 갈수없으면 뒤로 한칸가고 다시 1단계 근데 그 뒤도 바다면 그냥 멈춘다.

n, m = map(int, input().split())

# 방문위치 저장용
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽회전


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

#       북(0)
#   서(3)   동(1)
#       남(2)
# 기본 왼쪽90도 회저능ㄹ -= 1로 지정해두고,
# 동의 왼쪽90도는 -1하면 0 (북)
# 남의 왼쪽90도는 -1하면 1 (동)
# 서의 왼쪽90도는 -1하면 2 (남)
# 북의 왼쪽90도는 따로 지정해서 -1이면 3(서)로 바로 갈수있도록 지정.


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
